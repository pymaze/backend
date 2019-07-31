from django.contrib import admin
from django.urls import path, include
from rooms import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('users.urls', namespace='users')),
    path('api/rooms/', views.all_rooms)

]
