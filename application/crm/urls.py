from django.urls import include, path
from crm import views

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"", views.LoginViewSet, basename="login")
router.register(r"", views.SmsView, basename="sms")


urlpatterns = [
    path("", include(router.urls)),
]
