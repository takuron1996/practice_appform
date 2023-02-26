from django.urls import include, path

from . import views

# from rest_framework import routers


# router = routers.DefaultRouter()
# router.register(r"sms", views.SmsViewSet, basename="sms")

urlpatterns = [
    # path("", include(router.urls)),
    path("sms/", views.SmsView.as_view(), name="sms")
]
