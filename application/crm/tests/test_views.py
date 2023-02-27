from unittest.mock import Mock

import pytest
from rest_framework import status

from common.sms import SnsResource
from crm.injectors import injector


@pytest.fixture
def mock_sns_resouce_success():
    sms = Mock()
    sms.meta.client.publish.return_value = {"MessageId": "success"}
    return sms


def test_sms_view(api_client, mock_sns_resouce_success):
    injector.binder.bind(SnsResource, to=mock_sns_resouce_success)
    phone_number = "09051321996"
    message = "test送信"
    data = {"phone_number": phone_number, "message": message}
    response = api_client.post("/api/sms/", data, format="json")
    assert response.status_code == status.HTTP_200_OK
    assert response.data == {"message_id": "success"}
