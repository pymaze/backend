import jwt
from datetime import datetime, timedelta
from django.conf import settings
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, PermissionsMixin, BaseUserManager)


class UserManager(BaseUserManager):

    def create_user(self, username, password=None, current_room=None):
        """
        Create and return a 'User' with username and password. Sets current_room to None by default.
        """
        if username is None:
            raise TypeError('Users must have a username.')

        user = self.model(username=username)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, password, current_room=None, **extra_fields):
        """
        Create and return a 'User' with superuser permissions.
        """
        if password is None:
            raise TypeError('Superusers must have a password.')
        user = self.create_user(username, password)
        user.is_superuser = True
        user.is_staff = True

        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):
    """
    An abstract base class implementing a fully featured User model
    with admin-compliant permissions.
    Also contains the current_room property detailing which room the active user is in.
    """

    # Naive approach setting the username as the primary key, but as is
    # we don't want to allow users to change their username, only the room
    # their character is currently in
    username = models.CharField(
        db_index=True, max_length=255, unique=True, primary_key=True)
    current_room = models.CharField(max_length=255, default="start")

    USERNAME_FIELD = 'username'
    objects = UserManager()

    def __str__(self):
        return f'username: {self.username}, current_room: {self.current_room}'

    @property
    def token(self):
        return self._generate_jwt_token()

    def _generate_jwt_token(self):
        dt = datetime.now() + timedelta(days=60)
        token = jwt.encode({
            'id': self.pk,
            'exp': int(dt.strftime('%s'))
        }, settings.SECRET_KEY, algorithm='HS256')

        return token.decode('utf-8')
