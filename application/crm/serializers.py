"""シリアライザーの定義モジュール
"""
from django.core.validators import RegexValidator
from rest_framework import serializers

from crm.enums import UserRole
from crm.models import Customer, User


class SmsSerializer(serializers.Serializer):
    """SMS用のシリアライザ"""

    phone_regex = RegexValidator(
        regex=r"^\d+$",
        message="電話番号の形式は0123456789",
    )
    """電話番号(日本)のバリデータ"""

    phone_number = serializers.CharField(
        validators=[phone_regex], max_length=11
    )
    """電話番号(日本)"""

    message = serializers.CharField()
    """送信するメッセージ"""


class LoginSerializer(serializers.Serializer):
    """ログイン処理用のシリアライザ"""

    employee_number = serializers.CharField(max_length=8)
    """社員番号"""
    password = serializers.CharField(max_length=255)
    """パスワード"""


class CustomerSerializer(serializers.ModelSerializer):
    """顧客情報用のシリアライザ"""

    phone_regex = RegexValidator(
        regex=r"^\d+$",
        message="電話番号の形式は0123456789",
    )
    """電話番号(日本)のバリデータ"""

    phone_number = serializers.CharField(
        validators=[phone_regex], max_length=11
    )
    """電話番号(日本)"""

    class Meta:
        model = Customer
        fields = "__all__"
        read_only_fields = ("id", "created_at")


class CreateUserSerializer(serializers.ModelSerializer):
    """ユーザー生成用のシリアライザ"""

    user_role = serializers.ChoiceField(
        choices=[(tag.value, tag.name) for tag in UserRole]
    )
    # """ユーザー権限"""

    class Meta:
        model = User
        fields = "__all__"
        read_only_fields = (
            "id",
            "is_staff",
            "is_superuser",
            "groups",
            "user_permissions",
            "verified",
        )


class ListUserSerializer(serializers.ModelSerializer):
    """ユーザー一覧用のシリアライザ"""

    def to_representation(self, instance):
        """groupsをidから名前に変換"""
        ret = super(ListUserSerializer, self).to_representation(instance)
        ret["groups"] = instance.groups.name
        return ret

    class Meta:
        model = User
        exclude = ("password",)
        read_only_fields = (
            "id",
            "is_staff",
            "is_superuser",
            "groups",
            "user_permissions",
            "verified",
        )
