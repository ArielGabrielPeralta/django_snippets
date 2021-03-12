from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from .models import User


class RegisterForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["email", ]

    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = User.object.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("Email has been register")
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("The password didn't match")
        return password2


class RegisterAdminForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ("username", "email", "first_name", "last_name")

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("The password didn't match")
        return password2

    def save(self, commit=True):
        user = super(RegisterAdminForm, self).save(commit=False)
        if commit:
            user.save()
        return user


class UpdateAdminForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ("email", "username", "password", "first_name", "last_name")

    def clean_password(self):
        return self.initial['password']
