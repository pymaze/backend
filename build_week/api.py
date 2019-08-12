from pusher import Pusher
from django.http import JsonResponse
from decouple import config
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
import json
from time import gmtime, strftime
from users.models import User

# instantiate pusher
pusher = Pusher(app_id=config('PUSHER_APP_ID'), key=config(
    'PUSHER_APP_KEY'), secret=config('PUSHER_APP_SECRET'), cluster=config('PUSHER_CLUSTER'))


@csrf_exempt
@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def say(request):
    try:
        user = User.objects.get(username=request.data.get('username'))
    except User.DoesNotExist:
        print('That user does not exist')
        return JsonResponse({'error': 'That user does not exist'})
    print(f'user: {user}')
    message = request.data.get('message', '')
    print(f'message: {message}')
    time = strftime("%m-%d-%Y %H:%M:%S", gmtime())
    nearby_players = [u.username for u in User.objects.all(
    ) if u.current_room == user.current_room and u.username != user.username]
    print("nearby players: ", nearby_players)
    return JsonResponse({'message': message})
