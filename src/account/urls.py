from django.urls import include, path
from rest_framework import routers

from .views import UserViewSet

router = routers.DefaultRouter()
router.register(r"user", UserViewSet)

app_name = "account"

urlpatterns = [
    path("", include(router.urls)),
]
