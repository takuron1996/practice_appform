from logging import getLogger

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, JsonResponse
from drf_spectacular.utils import (OpenApiExample, OpenApiResponse,
                                   extend_schema)
from rest_framework import mixins, status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import OR, AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from common.constant import LoggerName
from common.sms import SnsWrapper
from common.utils import get_client_ip
from crm.enums import UserRole
from crm.filters import CustomerFilter
from crm.injectors import injector
from crm.models import Customer, User
from crm.permissions import IsAdmin, IsApprover, IsManagement
from crm.serializers import (CreateUserSerializer, CustomerSerializer,
                             ListUserSerializer, LoginSerializer,
                             SmsSerializer)

application_logger = getLogger(LoggerName.APPLICATION.value)
emergency_logger = getLogger(LoggerName.EMERGENCY.value)


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
class SmsViewSet(ViewSet):
    """SMS関連のViewSet"""

    serializer_class = SmsSerializer
    permission_classes = [IsAuthenticated]

    @action(methods=["post"], detail=False)
    def sms(self, request):
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
    """ログイン関連のViewSet"""

    serializer_class = LoginSerializer
    permission_classes = [AllowAny]

    @extend_schema(
        request=LoginSerializer,
        examples=[
            OpenApiExample(
                "ログイン",
                summary="ログイン",
                value={"employee_number": "00000001", "password": "test"},
                request_only=True,
                response_only=False,
                description="一般ユーザ",
            )
        ],
        responses=OpenApiResponse(
            status.HTTP_200_OK,
            description="グループの種類",
            examples=[
                OpenApiExample(
                    "groups",
                    summary="groups",
                    value={"groups": "管理者"},
                    request_only=False,
                    response_only=True,
                    description="管理者権限",
                )
            ],
        ),
    )
    @action(methods=["post"], detail=False)
    def login(self, request):
        """ログイン機能"""
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user: User = authenticate(**serializer.data)
        if not user:
            application_logger.warning(
                f"ログイン失敗:{serializer.data.get('employee_number')}, IP: {get_client_ip(request)}"
            )
            return JsonResponse(
                data={"msg": "ユーザーまたはパスワードが間違っています。"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        login(request, user)
        application_logger.info(
            f"ログイン成功: {user}, IP: {get_client_ip(request)}"
        )
        return JsonResponse(data={"groups": f"{user.groups.name}"})

    @extend_schema(request=None, responses={status.HTTP_200_OK: None})
    @action(methods=["post"], detail=False)
    def logout(self, request):
        """ログアウト"""
        application_logger.info(
            f"ログアウト: {request.user}, IP: {get_client_ip(request)}"
        )
        logout(request)
        return HttpResponse(status=status.HTTP_200_OK)


@extend_schema(
    request=CustomerSerializer,
    examples=[
        OpenApiExample(
            "customer",
            summary="顧客情報登録",
            value={
                "phone_number": "09051321996",
                "name": "池上 拓",
                "birth_of_date": "1996-05-04",
            },
            request_only=True,
            response_only=False,
            description="顧客情報登録",
        )
    ],
    responses=OpenApiResponse(
        status.HTTP_200_OK,
        description="顧客情報",
        examples=[
            OpenApiExample(
                "message_id",
                summary="message_id",
                value={
                    "id": "01GVJWMBN4Y2J4NW92CYJZVT7E",
                    "phone_number": "09051321996",
                    "name": "池上 拓",
                    "birth_of_date": "1996-05-04",
                    "created_at": "2023-03-16T00:01:18.137946+09:00",
                },
                request_only=False,
                response_only=True,
                description="顧客情報",
            )
        ],
    ),
)
class CustomerViewSet(
    mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet
):
    """顧客情報関連のViewSet"""

    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [AllowAny]
    filterset_class = CustomerFilter


class HealthViewSet(ViewSet):
    """ヘルスチェック用のViewSet"""

    @action(methods=["get"], detail=False, permission_classes=[AllowAny])
    def health(self, request):
        """ヘルスチェック"""
        return JsonResponse(data={"status": "pass"}, status=status.HTTP_200_OK)


class UserViewSet(
    viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin
):
    """ユーザー用のViewSet"""

    queryset = User.objects.all()

    def get_permissions(self):
        match self.action:
            case "list":
                permission_classes = [AllowAny()]
            case _:
                permission_classes = [
                    OR(OR(IsAdmin(), IsManagement()), IsApprover())
                ]
        return permission_classes

    def get_serializer_class(self):
        """ViewSetアクション毎にシリアライザを変更する"""

        match self.action:
            case "create":
                return CreateUserSerializer
            case _:
                return ListUserSerializer

    def create(self, request, *args, **kwargs):
        """ユーザーを作成"""
        serializer = self.get_serializer_class()(data=request.data)
        if not serializer.is_valid():
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )

        User.objects.create_user(
            name=serializer.validated_data["name"],
            employee_number=serializer.validated_data["employee_number"],
            password=serializer.validated_data["password"],
            group=UserRole(serializer.validated_data.get("user_role")),
        )

        return Response(status=status.HTTP_201_CREATED)
