from django import forms
from django.contrib.auth.forms import UserCreationForm

from EcoApp.models import User, Customer, Dealer, Authority, Scrap


class UserRegister(UserCreationForm):
    username = forms.CharField()
    password1 = forms.CharField(label='password',widget=forms.PasswordInput)
    password2 = forms.CharField(label='password',widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username','password1','password2')

class customerform(forms.ModelForm):
    class Meta:
        model = Customer
        exclude = ('user','approval_status')

class dealerform(forms.ModelForm):
    class Meta:
        model = Dealer
        exclude = ('user','approval_status')

class authorityform(forms.ModelForm):
    class Meta:
        model = Authority
        exclude = ('user','approval_status')

class Scrapform(forms.ModelForm):
    class Meta:
        model=Scrap
        exclude = ('approval_status',)
