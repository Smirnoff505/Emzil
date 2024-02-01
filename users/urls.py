from django.urls import path

from users.apps import UsersConfig
from users.views import LoginView, LogoutView, RegisterView, mail_verification, UserUpdateView

app_name = UsersConfig.name

urlpatterns = [
    path('', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('register/verification/<int:pk>', mail_verification, name='mail_verification'),
    path('profile/', UserUpdateView.as_view(), name='profile'),
]
