from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    # first_name = forms.CharField(required=True,validators=[
        
    # ])
    # last_name = forms.CharField(required=True)
    # email = forms.EmailField(required=True)
    # bio = forms.CharField(required=True,widget=forms.Textarea)
    dob = forms.DateField(required=True,widget=forms.DateInput(attrs={'type':'date'}))

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('first_name','last_name','email','bio','dob')

    
