from django import forms
from .models import Thread
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm, TextInput, EmailInput, PasswordInput, ImageField

class ThreadForm(forms.ModelForm):
    class Meta:
        model = Thread
        fields = ('text', 'photo')
        
        
class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder' : 'Email', 'class' : 'rounded-lg'}))
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        widgets = {
            'username' : TextInput(attrs={
                                   'class' : 'bg-[#201c1c] text-white rounded-lg'}),
            'email' : EmailInput(attrs={
                                   'class' : 'bg-[#201c1c] text-white rounded-lg'}),
            'password1' : PasswordInput(attrs={
                                   'class' : 'bg-[#201c1c] text-white rounded-lg'}),
            'password2' : PasswordInput(attrs={
                                   'class' : 'bg-[#201c1c] text-white rounded-lg'})
                                
        }
