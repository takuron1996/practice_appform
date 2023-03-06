from logging import getLogger

from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from drf_spectacular.utils import (OpenApiExample, OpenApiResponse,
                                   extend_schema)
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet

from common.constant import LoggerName
from common.sms import SnsWrapper
from common.utils import get_client_ip
from crm.models import User

from .injectors import injector
from .serializers import LoginSerializer, SmsSerializer


@extend_schema(
    request=SmsSerializer,
    examples=[
        OpenApiExample(
            "SMS",
            summary="SMS送信",
            value={"phone_number": "09051321996", "message": "test送信"},
            request_only=True,
            response_only=False,
            description="SMS送信を実施",
        )
    ],
    responses=OpenApiResponse(
        status.HTTP_200_OK,
        description="SMS送信が成功した場合",
        examples=[
            OpenApiExample(
                "message_id",
                summary="message_id",
                value={"message_id": "TESTSUCESS"},
                request_only=False,
                response_only=True,
                description="メッセージのID",
            )
        ],
    ),
)
class SmsView(APIView):
    """SMS関連のView"""

    serializer_class = SmsSerializer

    def post(self, request):
        """SMSの送信処理"""
        serializer = self.serializer_class(data=request.data)
        if not serializer.is_valid():
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )
        sms = injector.get(SnsWrapper)
        message_id = sms.publish_text_message(
            "+81" + serializer.validated_data["phone_number"],
            serializer.validated_data["message"],
        )
        return Response({"message_id": message_id}, status=status.HTTP_200_OK)


class LoginViewSet(ViewSet):
    """ログイン関連のView"""

    serializer_class = LoginSerializer
    application_logger = getLogger(LoggerName.APPLICATION.value)
    emergency_logger = getLogger(LoggerName.EMERGENCY.value)

    @action(methods=["post"], detail=False, permission_classes=[])
    def login(self, request):
        """ログイン機能"""
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user: User = authenticate(**serializer.data)
        if not user:
            self.application_logger.warning(
                f"ログイン失敗:{serializer.data.get('employee_number')}, IP: {get_client_ip(request)}"
            )
            return JsonResponse(
                data={"msg": "ユーザーまたはパスワードが間違っています。"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        login(request, user)
        self.application_logger.info(
            f"ログイン成功: {user}, IP: {get_client_ip(request)}"
        )
        return JsonResponse(data={"role": user.Role(user.role).name})
