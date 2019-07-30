from rest_framework import serializers

from .models import User


class RegistrationSerializer(serializers.ModelSerializer):
    """Serializes registration requests and creates a new user."""

    # Passwords between 8 and 128 chars, not readable
    password = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True
    )
    # Client shoudln't be able to send a token with a registration
    # request. Token being read-only handles this.
    token = serializers.CharField(max_length=255, read_only=True)

    class Meta:
        model = User
        # list all fields that could possible be included in a request
        # or response
        fields = ['username', 'password', 'token']

    def create(self, validated_data):
        # Use the 'create_user' method to create a new user
        return User.objects.create_user(**validated_data)
