from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response

from users.models import User
from users.serializer import UserSerializer


class UserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        print(request.data)
        return Response(status=status.HTTP_201_CREATED)
