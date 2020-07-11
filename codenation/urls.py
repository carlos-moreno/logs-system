from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from codenation.account.views import UserViewSet
from codenation.core.views import AgentViewSet, EventViewSet

router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('agents', AgentViewSet)
router.register('events', EventViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls'))
]
