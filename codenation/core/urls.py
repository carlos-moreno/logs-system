from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from codenation.core.views import AgentViewSet, EventViewSet

router = routers.DefaultRouter()
router.register('agents', AgentViewSet, basename='agent')
router.register('events', EventViewSet)

urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
