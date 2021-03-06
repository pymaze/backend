from django.urls import path

from .views import RegistrationAPIView, LoginAPIView, UserView

app_name = 'users'
urlpatterns = [
    path('users/', RegistrationAPIView.as_view()),
    path('users/login/', LoginAPIView.as_view()),
    path('users/move/', UserView.as_view())
]
