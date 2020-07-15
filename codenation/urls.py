from django.contrib import admin
from django.urls import path, include

from codenation.core.views import documentation_api

urlpatterns = [
    path('', documentation_api, name="documentation"),
    path('api/v1/', include('codenation.urls_api')),
    path('admin/', admin.site.urls),

]
