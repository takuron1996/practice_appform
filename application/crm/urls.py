from django.urls import include, path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r"login", views.LoginViewSet, basename="login")
# router.register(r"sms", views.SmsViewSet, basename="sms")

urlpatterns = [
    path("login/", include(router.urls)),
    path("sms/", views.SmsView.as_view(), name="sms"),
]
