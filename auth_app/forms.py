from django import forms
from django.contrib.auth.forms import UserCreationForm
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
            })

            }
