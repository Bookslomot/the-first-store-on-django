from django.contrib.auth.views import LogoutView
from django.urls import path

from account.views import LoginUser, RegistrationView, ProfileView

urlpatterns = [
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('registration/', RegistrationView.as_view(), name='registration'),
    path('profile/', ProfileView.as_view(), name='profile'),

]