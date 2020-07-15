from django.urls import path, include
from rest_framework import routers

from codenation.core.views import AgentViewSet, EventViewSet
from codenation.account.views import UserViewSet

router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('agents', AgentViewSet)
router.register('events', EventViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
