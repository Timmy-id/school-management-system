from django.urls import path, include
from rest_framework import routers
from .views import WaitlistEntryViewSet


router = routers.DefaultRouter()
router.register(r'', WaitlistEntryViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
