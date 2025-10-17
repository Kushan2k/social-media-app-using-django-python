from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,PasswordChangeForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):

    password1 = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(attrs={
            "class": "w-full px-3 py-2 mb-3 text-sm leading-tight text-gray-700 border rounded shadow appearance-none focus:outline-none focus:shadow-outline",
            "placeholder": "***********",
            "id": "password",
        }),
    )

    password2 = forms.CharField(
        label="Confirm Password",
        strip=False,
        widget=forms.PasswordInput(attrs={
            "class": "w-full px-3 py-2 mb-3 text-sm leading-tight text-gray-700 border rounded shadow appearance-none focus:outline-none focus:shadow-outline",
            "placeholder": "Re-enter password",
            "id": "confirmPassword",
        }),
    )

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('first_name','last_name','email','password1',
                                                'password2','bio','dob')

        widgets={
            "first_name":forms.TextInput(attrs={
                "class":"w-full px-3 py-2 text-sm leading-tight text-gray-700  border rounded shadow appearance-none focus:outline-none focus:shadow-outline",
                "placeholder":"First Name",
                "id":"firstName"

            }),
            "last_name":forms.TextInput(attrs={
                "class":"w-full px-3 py-2 text-sm leading-tight text-gray-700  border rounded shadow appearance-none focus:outline-none focus:shadow-outline",
                "placeholder":"Last Name",
                "id":"lastName"
            }),
            "email":forms.EmailInput(attrs={
                "class":"w-full px-3 py-2 text-sm leading-tight text-gray-700  border rounded shadow appearance-none focus:outline-none focus:shadow-outline",
                "placeholder":"Email",
                "id":"email",
                "type":"email"
            }),
            
            "bio":forms.Textarea(attrs={
                "class":"w-full px-3 py-2 text-sm leading-tight text-gray-700  border rounded shadow appearance-none focus:outline-none focus:shadow-outline",
                "placeholder":"Bio",
                "id":"bio",
                "rows":"3"
            }),
            "dob":forms.DateInput(attrs={
                "class":"w-full px-3 py-2 text-sm leading-tight text-gray-700  border rounded shadow appearance-none focus:outline-none focus:shadow-outline",
                "id":"dob",
                "type":"date"
            }),
            "username":forms.TextInput(attrs={
                "class":"w-full px-3 py-2 text-sm leading-tight text-gray-700  border rounded shadow appearance-none focus:outline-none focus:shadow-outline",
                "placeholder":"Username",
                "id":"username"
            }),
        }



class CustomLoginForm(AuthenticationForm):


    username = forms.EmailField(
        widget=forms.EmailInput(attrs={
            "class": "w-full px-3 py-2 mb-3 text-sm leading-tight text-gray-700 border rounded shadow appearance-none focus:outline-none focus:shadow-outline",
            "placeholder": "Email",
            "id": "email",
            "type": "email"
        }),
        label="Email"
    )

    password = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(attrs={
            "class": "w-full px-3 py-2 mb-3 text-sm leading-tight text-gray-700 border rounded shadow appearance-none focus:outline-none focus:shadow-outline",
            "placeholder": "*****",
            "id": "password",
        }),
    )

    def confirm_login_allowed(self, user):
        
        if not user.is_active:
            raise forms.ValidationError(
                "This account is inactive. Please verify your account.",
                code='inactive',
            )
        

class CustomPasswordChangeForm(PasswordChangeForm):

    old_password = forms.CharField(
        label="Old Password",
        strip=False,
        widget=forms.PasswordInput(attrs={
            "class": "w-full px-3 py-2 mb-2 text-sm leading-tight text-gray-700 border rounded shadow appearance-none focus:outline-none focus:shadow-outline",
            "placeholder": "Old Password",
            "id": "old_password",
        }),
    )

    new_password1 = forms.CharField(
        label="New Password",
        strip=False,
        widget=forms.PasswordInput(attrs={
            "class": "w-full px-3 py-2 mb-2 text-sm leading-tight text-gray-700 border rounded shadow appearance-none focus:outline-none focus:shadow-outline",
            "placeholder": "New Password",
            "id": "new_password1",
        }),
    )

    new_password2 = forms.CharField(
        label="Confirm New Password",
        strip=False,
        widget=forms.PasswordInput(attrs={
            "class": "w-full px-3 py-2 mb-2 text-sm leading-tight text-gray-700 border rounded shadow appearance-none focus:outline-none focus:shadow-outline",
            "placeholder": "Confirm New Password",
            "id": "new_password2",
        }),
    )
        