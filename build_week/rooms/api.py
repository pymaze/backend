from rest_framework import serializers, viewsets
from .models import Room


class RoomsSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Room
        fields = ('destinationRoom', 'direction')


class PersonalRoomsViewSet(viewsets.ModelViewSet):
    serializer_class = RoomsSerializer
    queryset = Room.objects.all()
