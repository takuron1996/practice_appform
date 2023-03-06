from django.urls import include, path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r"", views.LoginViewSet, basename="login")

urlpatterns = [
    path("", include(router.urls)),
    path("sms/", views.SmsView.as_view(), name="sms"),
]
