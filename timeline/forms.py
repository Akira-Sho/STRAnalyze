from django import forms 
from .models import Post,Item,Like
from accounts.models import CustomUser

class PostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PostForm, self). __init__(*args,**kwargs)
        self.fields['photo'].widget.clear_checkbox_label= '←画像を削除する'
        
    class Meta:
        model = Post
        fields = ('text','photo',)
        widgets = {
            'text' : forms.Textarea(attrs={'placeholder': '投稿内容を入力してください','rows':4, 'cols':15,}),
        }
    
class BrandSearchForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('brand_name',)


