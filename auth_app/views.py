import string
from django.utils.timezone import now

from django.shortcuts import render,redirect
from django.http import HttpRequest,HttpResponse
from django.views import View
from .forms import CustomUserCreationForm
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.utils.crypto import get_random_string

User=get_user_model()

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
                
                if user.is_active:
                    messages.warning(req,"Account already exist,Please login!")
                    return redirect('sign-in')
                
                if user.verification_code and user.verification_code_created_at:
                    
                    
                    time_diff=now()-user.verification_code_created_at
                    if time_diff.total_seconds()<(10*60):
                        messages.warning(req,"A verification email has already been sent to your email,Please check your inbox!")
                        return redirect('sign-up')
                code=get_random_string(length=6,allowed_chars=string.ascii_letters+string.digits)
                user.verification_code=code
                user.verification_code_created_at=now()
                user.save()
                messages.warning(req,"Account already exist,Resending the verification email!")
                return redirect('sign-up')

                

            user=form.save(commit=False)
            user.is_active=False
            verification_code=get_random_string(length=6,allowed_chars=string.ascii_letters+string.digits)
            user.verification_code=verification_code
            user.verification_code_created_at=user.created_at
            

            user.save()
            # from .common.tasks import send_mail_with_template
            # import asyncio
            # loop=asyncio.new_event_loop()
            # asyncio.set_event_loop(loop)
            # loop.run_until_complete(send_mail_with_template(user.email,user.activation_token))
            messages.success(req,"Account created successfully,Please check your email to verify your account!")
            return redirect('index')
        else:
            
            messages.error(req,"Please correct the errors below.")
            return render(req,'sign-up.html',{'form':form})