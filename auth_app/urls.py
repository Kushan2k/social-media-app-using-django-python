from django.urls import path
from . import views


urlpatterns = [
    path('sign-up', views.SignIn.as_view(), name='sign_up'),
]