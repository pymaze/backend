from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404

from .serializers import RegistrationSerializer, LoginSerializer, UserSerializer
from .renderers import UserJSONRenderer
from .models import User


class RegistrationAPIView(APIView):
    # Allow any user (authed or not) to hit this endpoint
    permission_classes = (AllowAny,)
    renderer_classes = (UserJSONRenderer,)
    serializer_class = RegistrationSerializer

    def post(self, request):
        user = request.data.get('user', {})

        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class LoginAPIView(APIView):
    permission_classes = (AllowAny,)
    renderer_classes = (UserJSONRenderer,)
    serializer_class = LoginSerializer

    def post(self, request):

        user = request.data.get('user', {})
        # Call validate since serializer.save doesn't have anything to save
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class UserView(APIView):
    permission_classes = (IsAuthenticated,)

    def put(self, request):
        # First grab user passed in with the PUT request
        user = request.data.get('user', {})

        # Grab user from the database matching that unique username
        saved_user = get_object_or_404(User.objects.all(), pk=user['username'])

        # Update the data via serializer, validate, and return
        serializer = UserSerializer(
            instance=saved_user, data=user, partial=True)
        if serializer.is_valid(raise_exception=True):
            updated_user = serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
