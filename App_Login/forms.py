from dataclasses import field
from pyexpat import model
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from App_Login.models import UserProfile

class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="Email Address",required=True)
    
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class UserProfileChange(UserChangeForm):
    password = None
    class Meta:
        model = User
        # fields = ('username','email', 'first_name','last_name')
        fields = ('email', 'first_name','last_name')

class ProfilePic(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('profile_pic',)
class ProfileInfo(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('city','country','about')
        widgets = {
            'about': forms.Textarea(attrs={'class':'form-control', 'rows':'4'})
        }