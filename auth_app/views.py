from django.shortcuts import render,redirect
from django.http import HttpRequest


def index(req:HttpRequest):
    return render(req,'index.html')

# Create your views here.
def sign_up(req:HttpRequest):

    if req.user.is_authenticated:
        return redirect('/')

    return render(req, 'auth_app/sign-up.html')