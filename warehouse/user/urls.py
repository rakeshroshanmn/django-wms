from django.urls import path, include
from . import views as user_views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', user_views.signin , name = 'signin'),
    path('signout/', auth_views.LogoutView.as_view(), name='signout'),
]