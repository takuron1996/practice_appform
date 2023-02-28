"""viewsのテスト用モジュール"""
from unittest.mock import Mock

import pytest
from rest_framework import status

from common.sms import SnsResource
from crm.injectors import injector


@pytest.fixture
def mock_sns_resouce_success():
    """正常処理用のmoc

    Returns:
        Mock: SMSのMock
    """
    sms = Mock()
    sms.meta.client.publish.return_value = {"MessageId": "success"}
    return sms


def test_sms_view(api_client, mock_sns_resouce_success):
    """SMS送信機能の正常処理のテスト

    Args:
        api_client (APIClient): APIのクライアント
        mock_sns_resouce_success (Mock): SMSのMock
    """
    injector.binder.bind(SnsResource, to=mock_sns_resouce_success)
    phone_number = "09051321996"
    message = "test送信"
    data = {"phone_number": phone_number, "message": message}
    response = api_client.post("/api/sms/", data, format="json")
    assert response.status_code == status.HTTP_200_OK
    assert response.data == {"message_id": "success"}


def test_sms_view_valid_error_no_number(api_client, mock_sns_resouce_success):
    """SMS送信機能で電話番号がバリデーションエラーの場合（数字以外）

    Args:
        api_client (APIClient): APIのクライアント
        mock_sns_resouce_success (Mock): SMSのMock
    """
    injector.binder.bind(SnsResource, to=mock_sns_resouce_success)
    phone_number = "a9051321996"
    message = "test送信"
    data = {"phone_number": phone_number, "message": message}
    response = api_client.post("/api/sms/", data, format="json")
    assert response.status_code == status.HTTP_400_BAD_REQUEST
