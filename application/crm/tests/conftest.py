import pytest
from django.core.management import call_command
from rest_framework.test import APIClient


@pytest.fixture
def api_client():
    """APIのクライアント

    Returns:
        APIClient: APIのクライアント
    """
    return APIClient()


@pytest.fixture(scope="session")
def django_db_setup(django_db_setup, django_db_blocker):
    with django_db_blocker.unblock():
        call_command("loaddata", "crm.json")


@pytest.fixture(scope="session")
def general_login_user_data():
    return {
        "employee_number": "00000001",
        "password": "test",
    }
