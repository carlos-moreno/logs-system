from django.contrib import admin
from django.urls import path, include
from rest_framework.documentation import include_docs_urls

API_TITLE = 'API Logs System'
API_DESCRIPTION = 'Documentation Logs System API'

urlpatterns = [
    path('', include_docs_urls(title=API_TITLE, description=API_DESCRIPTION)),
    path('api/v1/', include('codenation.core.urls')),
    path('admin/', admin.site.urls),
]
