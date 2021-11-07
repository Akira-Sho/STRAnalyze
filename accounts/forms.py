from django import forms
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.conf import settings

from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from allauth.account.forms import LoginForm, SignupForm, ResetPasswordForm, ResetPasswordKeyForm

class MyLoginForm(LoginForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        """
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control form-control-sm'
        """
CustomUser = get_user_model()

subject = "登録確認"
message_template = """
ご登録ありがとうございます。
以下URLをクリックして登録を完了してください。

"""

def get_activate_url(user):
    uid = urlsafe_base64_encode(force_bytes(user.pk))
    token = default_token_generator.make_token(user)
    return settings.FRONTEND_URL + "/activate/{}/{}/".format(uid, token)

class MySignUpForm(SignupForm):
    def __init__(self, *args, **kwargs):
        super(MySignUpForm,self).__init__(*args, **kwargs)
        for field in self.fields.values():
                field.widget.attrs['class'] = 'form-control-sm'
    class Meta:
            model = CustomUser
            fields = ("username","email","password1","password2")
                
    def save(self, commit=True):
            # commit=Falseだと、DBに保存されない
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        # 確認するまでログイン不可にする
        user.is_active = False
        
        if commit:
            user.save()
            activate_url = get_activate_url(user)
            message = message_template + activate_url
            user.email_user(subject, message)
        return user

class ProfileForm(forms.ModelForm):
#form-controlクラスの属性の追加
    def __init__(self, *args, **kwargs):
        super(ProfileForm, self). __init__(*args,**kwargs)
        
        
        """
        for field in self.fields.values():
                field.widget.attrs['class'] = 'form-control'
        """
            
    class Meta:
            model = CustomUser
            fields = ('username','description','photo','age','gender','position','history','activity_area')
            help_texts = {
                'username': None,
            }
            
    