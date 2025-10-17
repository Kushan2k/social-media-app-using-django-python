from django.urls import path
from . import views,forms
from django.contrib.auth import views as auth_views
    
urlpatterns = [
    path('sign-up', views.SignIn.as_view(), name='sign_up'),
    path('sign-in', auth_views.LoginView.as_view(template_name='auth_app/accounts/login.html',), 
         name='sign_in',
         ),
    path('verify-account',view=views.VerifyAccount.as_view(),name='verify-account')

]
