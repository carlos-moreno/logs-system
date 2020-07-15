from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from codenation.core.views import documentation_api

urlpatterns = [
    path('', documentation_api, name="documentation"),
    path('api/v1/', include('codenation.urls_api')),
    path('admin/', admin.site.urls),
    path('get_token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh_token/', TokenRefreshView.as_view(), name='token_refresh'),
]
