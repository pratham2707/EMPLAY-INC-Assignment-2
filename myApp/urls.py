from django.urls import path
from myApp.views import *

urlpatterns = [
path('signup/', SignUpView.as_view(), name='signup'),
path('signin/', SignInView.as_view(), name='signin'),
path('profile/', UserProfileView.as_view(), name='profile'),
path('status/', StatusView.as_view(), name='status'),
]