from django.urls import path, include
from rest_framework import routers

from codenation.core.views import AgentViewSet, EventViewSet

router = routers.DefaultRouter()
router.register('agents', AgentViewSet)
router.register('events', EventViewSet)

urlpatterns = [
    path('api/v1/', include(router.urls)),
]
