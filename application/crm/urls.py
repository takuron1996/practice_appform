from django.urls import include, path
from rest_framework.routers import DefaultRouter

from crm import views

router = DefaultRouter()
router.register(r"", views.LoginViewSet, basename="login")
router.register(r"", views.SmsViewSet, basename="sms")
router.register(r"customer", views.CustomerViewSet, basename="customer")

health_router = DefaultRouter()
health_router.register(r"", views.HealthViewSet, basename="health")

urlpatterns = [
    path("", include(health_router.urls)),
    path("api/", include(router.urls)),
]
