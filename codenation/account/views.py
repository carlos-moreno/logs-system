from rest_framework import viewsets

from codenation.core.permissions import IsOwnerOrReadOnly
from .models import User
from .serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = (IsOwnerOrReadOnly,)

    queryset = User.objects.all()
    serializer_class = UserSerializer
