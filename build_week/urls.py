from django.contrib import admin
from django.urls import path, include
from rooms import views
from . import api


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('users.urls', namespace='users')),
    path('api/rooms/', views.RoomsView.as_view()),
    path('say/', api.say),
    path('shout/', api.shout),
    path('', views.RoomsView.index)

]
