"""シリアライザーの定義モジュール
"""
from django.core.validators import RegexValidator
from rest_framework import serializers

from crm.models import User


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
    password = serializers.CharField(max_length=255)
