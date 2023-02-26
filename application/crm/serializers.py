from rest_framework import serializers


class SmsSerializer(serializers.Serializer):
    """SMS用のシリアライザ"""

    phone_number = serializers.CharField()
    """電話番号"""

    message = serializers.CharField()
    """送信するメッセージ"""
