from drf_spectacular.utils import (OpenApiExample, OpenApiResponse,
                                   extend_schema)
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from common.sms import SnsWrapper

from .injectors import injector
from .serializers import SmsSerializer


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
