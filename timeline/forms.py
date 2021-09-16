from django import forms 
from .models import Post,ProductModel,Like
from accounts.models import CustomUser

class PostForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super(PostForm, self). __init__(*args,**kwargs)
        for field in self.fields.values():
                field.widget.attrs['class'] = 'form-control'
    #photo = forms.ImageField(widget=forms.ClearableFileInput())
    class Meta:
        model = Post
        fields = ('text','photo',)
    
    
class BrandSearchForm(forms.ModelForm):
    class Meta:
        model = ProductModel
        fields = ('brand',)

#↓今のところ使用しない使用しない
class ReviewSearchForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('age','history','gender',) #性別、年数,経験年数
