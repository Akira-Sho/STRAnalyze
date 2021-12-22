from django import forms
from .models import CustomUser
from allauth.account.forms import LoginForm, SignupForm, ResetPasswordForm, ResetPasswordKeyForm
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from timeline.widget import Image_Preview


class MyLoginForm(LoginForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

def get_activate_url(user):
    uid = urlsafe_base64_encode(force_bytes(user.pk))
    token = default_token_generator.make_token(user)
    return settings.FRONTEND_URL + "/activate/{}/{}/".format(uid, token)

class MySignUpForm(SignupForm):    
    class Meta:
            model = CustomUser
            fields = ("username","email","password1","password2")

class ProfileForm(forms.ModelForm):
    class Meta:
            model = CustomUser
            fields = ('username','description','photo','age','gender','position','history','activity_area')
            help_texts = {
                'username': None,
            }
            widgets = {
                'username' : forms.TextInput(attrs={'placeholder': 'この項目は入力必須です。'}),
                'photo': Image_Preview(include_preview=False),
            }