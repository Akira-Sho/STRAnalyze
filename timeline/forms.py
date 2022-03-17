from django import forms 
from .models import Post,Item,Like
from accounts.models import CustomUser
from .widget import Image_Preview
from django.conf import settings
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse


#レビュー投稿フォーム
class PostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PostForm, self). __init__(*args,**kwargs)
        self.fields['photo'].widget.clear_checkbox_label= '←選択したまま保存すると、'
        
    class Meta:
        model = Post
        fields = ('text','photo',)
        widgets = {
            'text' : forms.Textarea(attrs={'placeholder': '投稿内容を入力してください','rows':4, 'cols':15,}),
            'photo': Image_Preview(include_preview=False),
        }


#コンタクト送信フォーム
class ContactForm(forms.Form):
    name = forms.CharField(
        label='',
        max_length=20,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': "お名前",
        }),
    )
    email = forms.EmailField(
        label='',
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': "メールアドレス",
        }),
    )
    message = forms.CharField(
        label='',
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': "お問い合わせ内容",
        }),
    )

    def send_email(self):
        subject = "お問い合わせ"
        message = self.cleaned_data['message']
        name = self.cleaned_data['name']
        email = self.cleaned_data['email']
        from_email = '{name} <{email}>'.format(name=name, email=email)
        recipient_list = [settings.EMAIL_HOST_USER]  # 受信者リスト
        try:
            send_mail(subject, message, from_email, recipient_list)
        except BadHeaderError:
            return HttpResponse("無効なヘッダが検出されました。")

