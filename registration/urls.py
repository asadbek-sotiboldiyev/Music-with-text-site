from django.urls import path
from .views import *

urlpatterns = [
    path('login/', LoginPage, name='login_page'),
    path('logout/', Logout, name='logout_page'),
    path('signup/', SignUpPage, name='signup_page'),
]
