from django.urls import include, path
from rest_framework import routers

from .views import DriveFolderViewSet

router = routers.DefaultRouter()
router.register(r"folders", DriveFolderViewSet)

app_name = "drive"

urlpatterns = [
    path("", include(router.urls)),
]
