from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _


class RegisterForm(UserCreationForm):

    email = forms.EmailField(label='', widget=forms.EmailInput(attrs={'placeholder': _('Email')}))
    first_name = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': _('First name')}))
    last_name = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': _('Last name')}))
    password1 = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder': _('Password')}))
    password2 = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder': _('Confirm Password')}))

    class Meta:
        model = get_user_model()
        fields = ('email', 'first_name', 'last_name')
