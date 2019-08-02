from django.db import models
from django.contrib.postgres.fields import ArrayField


class RoomManager(models.Model):
    def create_room(self, n, e, s, w, title, description, players=[]):
        """
        Create and return a Room instance.
        """
        room = self.model(n=n, e=e, s=s, w=w, title=title,
                          description=description, players=players)
        room.save()
        return room


class Room(models.Model):
    """
    Room class which describes the player's surroundings. Contains info for
    connecting rooms, title and description, and a list of each player currently in the room.
    """
    n = models.IntegerField(default=0)
    e = models.IntegerField(default=0)
    s = models.IntegerField(default=0)
    w = models.IntegerField(default=0)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=500)
    players = ArrayField(models.CharField(max_length=255), blank=True)

    objects = RoomManager()

    def __str__(self):
        return f'Name: {title}, description: {description}, players: {players}'
