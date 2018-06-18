from django.shortcuts import render
from rest_framework import viewsets, status, generics, filters, permissions as prm
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import (IsAuthenticatedOrReadOnly,
IsAuthenticated, IsAdminUser )
from rest_framework.response import Response

from .models import UserProfile
from .serializers import UserProfileSerializer


class UserProfileViewSet(viewsets.ModelViewSet):
    """
    Handles creating, reading and updating profiles.
    """
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAdminUser,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', )


class LoginViewSet(viewsets.ViewSet, generics.GenericAPIView):
    """
    Log in using your username and password.
    **returns:** Token.
    """
    serializer_class = AuthTokenSerializer

    def create(self, request):
        """
        Use ObtainAuthToken APIView to validate and create token
        """
        return ObtainAuthToken().post(request)


class LogoutViewSet(viewsets.ViewSet):
    """
    Log out.
    """
    authentication_classes = (TokenAuthentication,)
    queryset = UserProfile.objects.all()
    permission_classes = (IsAuthenticated, )

    def create(self, request, format=None):
        """
        Log out.
        Operation deletes login token.
        """
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)  # TODO: нет импорта Response
