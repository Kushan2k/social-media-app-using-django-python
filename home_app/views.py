from django.shortcuts import render
from django.http import HttpRequest


def index(req:HttpRequest):
    return render(req,'index.html')
