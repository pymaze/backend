from rest_framework import serializers
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

from .models import User


class RegistrationSerializer(serializers.ModelSerializer):
    """Serializes registration requests and creates a new user."""

    # Passwords between 8 and 128 chars, not readable
    password = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True
    )
    # Client shouldn't be able to send a token with a registration
    # request. Token being read-only handles this.
    token = serializers.CharField(max_length=255, read_only=True)

    class Meta:
        model = User
        # list all fields that could possible be included in a request
        # or response
        fields = ['username', 'password', 'current_room', 'token']

    def create(self, validated_data):
        # Use the 'create_user' method to create a new user
        user = User.objects.create_user(**validated_data)
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=128, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)

    def validate(self, data):
        username = data.get('username', None)
        password = data.get('password', None)

        if username is None:
            raise serializers.ValidationError(
                f'A username is required to log in.'
            )
        if password is None:
            raise serializers.ValidationError(
                'A password is required to log in.'
            )

        user = authenticate(username=username, password=password)

        if user is None:
            raise serializers.ValidationError(
                'No user with that username and password was found.'
            )

        if not user.is_active:
            raise serializers.ValidationError(
                'This user has been deactivated.'
            )

        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'current_room', 'players']

    def update(self, instance, data):
        instance.username = data.get('username', instance.username)
        instance.current_room = data.get(
            'current_room', instance.current_room)
        instance.save()

        users = [u.username for u in User.objects.all(
        ) if u.current_room == instance.current_room and u.username != instance.username]
        instance.players = users

        return instance
