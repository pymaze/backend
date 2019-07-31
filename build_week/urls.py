from django.contrib import admin
from django.urls import path
from build_week.rooms import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/rooms/', views.all_rooms)

]
