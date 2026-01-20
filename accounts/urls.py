from django.urls import path , include
from django.contrib.auth.views import LoginView
from accounts.forms import UserLoginForm
from accounts.views import RegisterView , get_profile

urlpatterns = [
    path('login/' , LoginView.as_view(authentication_form = UserLoginForm) , name="login"),
    path('register/' , RegisterView.as_view() , name="register"),
    path('profile/' , get_profile, name="profile"),
    path('' , include('django.contrib.auth.urls'))
]

