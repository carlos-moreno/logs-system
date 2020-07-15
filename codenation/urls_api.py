from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from codenation.account.views import UserViewSet
from codenation.core.views import AgentViewSet, EventViewSet

router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('agents', AgentViewSet)
router.register('events', EventViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('get_token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh_token/', TokenRefreshView.as_view(), name='token_refresh'),
]
