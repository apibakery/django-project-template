from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from . import permissions
from .models import Hello
from .serializers import HelloSerializer


class HelloViewSet(viewsets.ModelViewSet):
    queryset = Hello.objects.all()
    serializer_class = HelloSerializer
    permission_classes = (
        IsAuthenticated,
        permissions.Hello,
    )
