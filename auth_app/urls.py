from django.urls import path
from . import views,forms
from django.contrib.auth import views as auth_views
    
urlpatterns = [
    path('sign-up', views.SignUp.as_view(), name='sign_up'),
    path('sign-in', auth_views.LoginView.as_view(template_name='login.html',), 
         name='sign-in',
         ),
    path('verify-account',view=views.VerifyAccount.as_view(),name='verify-account')

]
