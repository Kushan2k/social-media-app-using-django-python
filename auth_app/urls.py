from django.urls import path
from . import views,forms
from django.contrib.auth import views as auth_views
    
urlpatterns = [
    path('sign-up', views.SignUp.as_view(), name='sign_up'),
    path('sign-in', views.SignIn.as_view(), name='sign-in',),
    path('sign-out',auth_views.LogoutView.as_view(next_page='sign-in'),name='sign-out'),
    path('verify-account',view=views.VerifyAccount.as_view(),name='verify-account'),

    path("change-password",view=views.CustomPasswordChangeView.as_view(),name='change-password'),
    path('password-change/done',view=views.CustomPasswordChangeDoneView.as_view(),name='password-change-done'),
    path('password-reset',view=views.CustomPasswordResetView.as_view(),name='password-reset'),

]
