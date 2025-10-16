from django.shortcuts import render,redirect
from django.http import HttpRequest,HttpResponse
from django.views import View
from .forms import CustomUserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages

def index(req:HttpRequest):
    return render(req,'index.html')

# Create your views here.
class SignIn(View):

    def get(self,req:HttpRequest):

        form=CustomUserCreationForm()

        return render(req,'sign-up.html',{'form':form})
    
    def post(self,req:HttpRequest):

        form=CustomUserCreationForm(req.POST)

        if form.is_valid():

            user=User.objects.filter(email=form.cleaned_data['email']).first()

            if user:
                #TODO resend verification email
                
                messages.warning(req,"Account already exist,Resending the verification email!")
                return redirect('sign-up')

                

            user=form.save(commit=False)
            user.is_active=False
            
            user.save()
            from .common.tasks import send_mail_with_template
            import asyncio
            loop=asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            loop.run_until_complete(send_mail_with_template(user.email,user.activation_token))
            messages.success(req,"Account created successfully,Please check your email to verify your account!")
            return redirect('index')

        return render(req,'sign-up.html',{'form':form})