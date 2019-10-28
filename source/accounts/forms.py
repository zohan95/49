from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class SignUpForm(forms.Form):
    username = forms.CharField(max_length=100, required=True, label='Username')
    password = forms.CharField(max_length=100, required=True, label='Password',
                               widget=forms.PasswordInput)
    password_confirm = forms.CharField(max_length=100, required=True, label='Password confirm',
                                       widget=forms.PasswordInput)
    email = forms.EmailField(required=True, label='Email' )
    first_name = forms.CharField(max_length=100, label='First name', required=False)
    second_name = forms.CharField(max_length=100, label='Second Name', required=False)

    def clean_username(self):
        username = self.cleaned_data.get('username')
        try:
            User.objects.get(username=username)
            raise ValidationError('Username already taken.', code='username_taken')
        except User.DoesNotExist:
            return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        try:
            User.objects.get(email=email)
            raise ValidationError('Email already registered.', code='email_registered')
        except User.DoesNotExist:
            return email

    def clean_first_name(self):
        f_name = self.cleaned_data.get('first_name')
        s_name = self.cleaned_data.get('second_name')
        if not (f_name or s_name):
            raise ValidationError('Enter First or Second name')

    def clean(self):
        super().clean()
        password_1 = self.cleaned_data.get('password')
        password_2 = self.cleaned_data.get('password_confirm')
        if password_1 != password_2:
            raise ValidationError('Passwords do not match.', code='passwords_do_not_match')
        return self.cleaned_data


