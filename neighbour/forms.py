from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from . models import NeighbourHood,Post,Business,Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields= ['username','email','password1','password2']
        
User._meta.get_field('email')._unique=True

class HoodForm(forms.ModelForm):
    class Meta:
        model = NeighbourHood
        exclude = ('admin',)