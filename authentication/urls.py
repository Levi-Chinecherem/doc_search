from django.urls import path
from .views import user_login, user_signup, profile

urlpatterns = [
    path('login/', user_login, name='login'),
    path('signup/', user_signup, name='signup'),
    path('profile/', profile, name='account_profile'),
]
