"""シリアライザーのテスト用モジュール"""

from crm.serializers import SmsSerializer


def test_sms_serializer_valid():
    """正常な電話番号とメッセージを受け取ることができることを確認するテスト"""
    data = {"phone_number": "09012345678", "message": "Hello, World!"}
    serializer = SmsSerializer(data=data)
    assert serializer.is_valid() is True
    assert serializer.validated_data == data


def test_sms_serializer_invalid_phone_number():
    """不正な電話番号を受け取るとバリデーションエラーとなることを確認するテスト"""
    data = {"phone_number": "invalid_phone_number", "message": "Hello, World!"}
    serializer = SmsSerializer(data=data)
    assert serializer.is_valid() is False
    assert "phone_number" in serializer.errors


def test_sms_serializer_blank_phone_number():
    """電話番号が空文字列の場合にバリデーションエラーとなることを確認するテスト"""
    data = {"phone_number": "", "message": "Hello, World!"}
    serializer = SmsSerializer(data=data)
    assert serializer.is_valid() is False
    assert "phone_number" in serializer.errors


def test_sms_serializer_null_phone_number():
    """電話番号がnullの場合にバリデーションエラーとなることを確認するテスト"""
    data = {"phone_number": None, "message": "Hello, World!"}
    serializer = SmsSerializer(data=data)
    assert serializer.is_valid() is False
    assert "phone_number" in serializer.errors


def test_sms_serializer_blank_message():
    """メッセージが空文字列の場合にバリデーションエラーとなることを確認するテスト"""
    data = {"phone_number": "09012345678", "message": ""}
    serializer = SmsSerializer(data=data)
    assert serializer.is_valid() is False
    assert "message" in serializer.errors


def test_sms_serializer_null_message():
    """メッセージがnullの場合にバリデーションエラーとなることを確認するテスト"""
    data = {"phone_number": "09012345678", "message": None}
    serializer = SmsSerializer(data=data)
    assert serializer.is_valid() is False
    assert "message" in serializer.errors
