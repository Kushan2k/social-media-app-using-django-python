import string
from django.utils.timezone import now

from django.shortcuts import render,redirect
from django.http import HttpRequest
from django.views import View
from .forms import CustomUserCreationForm,CustomLoginForm,CustomPasswordChangeForm
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.utils.crypto import get_random_string
from .models import CustomUser
from .common.tasks import send_mail_with_template
from django.contrib.auth.views import LoginView,PasswordChangeView
from .mixins import RedirectAuthenticatedUserMixin
from django.contrib.auth.mixins import LoginRequiredMixin

User=get_user_model()

def index(req:HttpRequest):
    return render(req,'index.html')

# Create your views here.
class SignUp(RedirectAuthenticatedUserMixin,View):

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
            print(verification_code)
            user.verification_code_created_at=user.created_at
            

            user.save()
            messages.success(req,"Account created successfully,Please check your email to verify your account!")
            return redirect('verify-account')
        else:
            
            messages.error(req,"Please correct the errors below.")
            return render(req,'sign-up.html',{'form':form})



class SignIn(RedirectAuthenticatedUserMixin,LoginView):

    
   
    template_name = 'login.html'
    redirect_authenticated_user=True
    authentication_form=CustomLoginForm



class VerifyAccount(View):


    def get(self,req:HttpRequest):

        return render(req,'verify-account.html')
    
    def post(self,req:HttpRequest):

        code=req.POST.get('code',None)

        if not code or code=='':
            messages.error(req,"Verification code in required!")
            return redirect('verify-account')
        
        user:CustomUser=User.objects.filter(verification_code=code).first()

        if not user:
            messages.error(req,"User not found!")
            return redirect('verify-account')

        if user.is_verification_code_expired():
            messages.error(req,"Your Verification Code Has been expired!")
            return redirect('verify-account')

        user.is_active=True
        user.verification_code=None
        user.verification_code_created_at=None

        user.save()

        messages.success(req,"You Account has been verified!")

        context={
            "user": user,
            "username": getattr(user, "username", ""),
            
        }

        send_mail_with_template(
            context,
            "Account Verification",
            user.email,
            'emails/verification-success.html'
        )

        return redirect('sign-in')
    

class CustomPasswordChangeView(LoginRequiredMixin,PasswordChangeView):
    template_name = 'password-change.html'
    success_url = '/sign-in'
    form_class=CustomPasswordChangeForm
    