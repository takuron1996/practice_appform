from unittest.mock import Mock

import pytest
from botocore.exceptions import ClientError

from common.sms import SnsWrapper


@pytest.fixture
def mock_sns_resource():
    """sns_resourceのモック

    Returns:
        Mock: sns_resourceのモック
    """
    return Mock()


def test_publish_text_message_success(mock_sns_resource):
    """正常処理のテスト

    Args:
        mock_sns_resource (Mock): sns_resourceのモック
    """
    mock_publish = mock_sns_resource.meta.client.publish
    mock_publish.return_value = {"MessageId": "success"}

    sns = SnsWrapper(mock_sns_resource)
    phone_number = "+8109051321996"
    message = "test送信"
    response = sns.publish_text_message(phone_number, message)

    mock_publish.assert_called_with(PhoneNumber=phone_number, Message=message)
    assert response == "success"


def test_publish_text_message_failure(mock_sns_resource):
    """ClientErrorが起こる場合のテスト

    Args:
        mock_sns_resource (Mock): sns_resourceのモック
    """
    mock_publish = mock_sns_resource.meta.client.publish
    mock_publish.side_effect = ClientError({}, "Error")

    sns = SnsWrapper(mock_sns_resource)
    phone_number = "+8109051321996"
    message = "test送信"
    with pytest.raises(ClientError):
        sns.publish_text_message(phone_number, message)

    mock_publish.assert_called_with(PhoneNumber=phone_number, Message=message)
