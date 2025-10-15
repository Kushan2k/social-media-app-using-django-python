from django.shortcuts import render,redirect
from django.http import HttpRequest,HttpResponse
from django.views import View



def index(req:HttpRequest):
    return render(req,'index.html')

# Create your views here.
class SignIn(View):

    def get(self,req:HttpRequest):

        return render(req,'auth_app/sign-up.html')
    
    def post(self,req:HttpRequest):

        resp=HttpResponse()
        resp.status_code=201

        return resp