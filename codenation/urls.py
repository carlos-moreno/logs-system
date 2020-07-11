from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from codenation.account.views import UserViewSet
from codenation.core.views import AgentViewSet, EventViewSet

from rest_framework.documentation import include_docs_urls


API_TITLE = 'API Logs System'
API_DESCRIPTION = 'Documentation Logs System API'

router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('agents', AgentViewSet, basename='agent')
router.register('events', EventViewSet)

urlpatterns = [
    path('', include_docs_urls(title=API_TITLE, description=API_DESCRIPTION)),
    path('api/v1/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls'))
]
