from django.shortcuts import render

# Create your views here.

# /api/account/me -> shows user if logged in, else 403
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action
from django.http import Http404

from .models import User
from .serializer import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        return Response(UserSerializer(request.user).data)

    @action(detail=False, methods=['GET'])
    def me(self, request):
        return Response(UserSerializer(request.user).data)

    def retrieve(self, request, pk=None):
        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404("User does not exist")
        return Response(UserSerializer(user).data)