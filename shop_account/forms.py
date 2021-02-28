from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from captcha.fields import CaptchaField
from .models import *


message = {
    'required': 'this field is required',
    'invalid': 'please enter a valid email address',
    'ma_length': 'character for this field is too long'
}


class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email', 'username')

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('email', 'username')

    def clean_password(self):
        return self.initial["password"]


class SignInForm(forms.Form):
    email = forms.EmailField(max_length=77, error_messages=message, widget=forms.TextInput())
    password = forms.CharField(error_messages={'required': 'this field is required'}, widget=forms.PasswordInput())
    remember = forms.CharField(required=False, label='remember me', widget=forms.CheckboxInput())
    captcha = CaptchaField()


class SignUpForm(forms.Form):
    username = forms.CharField(max_length=77, error_messages=message, widget=forms.TextInput())
    email = forms.EmailField(max_length=77, error_messages=message, widget=forms.TextInput())
    password = forms.CharField(error_messages={'required': 'this field is required'}, widget=forms.PasswordInput())
    confirm_password = forms.CharField(error_messages={'required': 'this field is required'}, widget=forms.PasswordInput())

    def clean_username(self):
        username = self.cleaned_data['username']
        qs = User.objects.filter(username=username)
        if qs.exists():
            raise forms.ValidationError('this username is already exists')
        return username
    
    def clean_email(self):
        email = self.cleaned_data['email']
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError('this email address is already exists')
        return email
    
    def clean_confirm_password(self):
        password = self.cleaned_data['password']
        confirm_password = self.cleaned_data['confirm_password']
        if password != confirm_password:
            raise forms.ValidationError('Passwords must be mtach!')
        return confirm_password
    