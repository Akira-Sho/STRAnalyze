from django.db import models
from django.utils import timezone
from imagekit.models import ImageSpecField, ProcessedImageField
from imagekit.processors import ResizeToFill, ResizeToFit
from django.contrib.auth import get_user_model
from django.contrib.sessions.models import Session

RACKET_POSITION_CHOICES = [('後衛','後衛'),('前衛','前衛'),('前・後衛','前・後衛')] 
BRAND_CHOICES = [('YONEX','YONEX'),('MIZUNO','MIZUNO'),('DUNLOP','DUNLOP'),('GOSEN','GOSEN'),('SRIXON','SRIXON')] 

CustomUser = get_user_model()

class Post(models.Model):
	author = models.ForeignKey('accounts.CustomUser', on_delete=models.CASCADE)
	item = models.ForeignKey('timeline.Item', on_delete=models.CASCADE)
	slug = models.SlugField(verbose_name="URLスラッグ（英語）",null=True)
	text = models.TextField(verbose_name='本文',max_length=200,)
	photo = models.ImageField(verbose_name='写真', blank=True, null=True, upload_to='images/')
	post_photo = ImageSpecField(source='photo',processors=[ResizeToFit(1080, 1080)],format='JPEG',options={'quality':60})
	created_at = models.DateTimeField(default=timezone.now)
	#必要に応じてlike数を上下させるカラムを追加する
	class Meta:
    		ordering = ['-created_at']
 
class Like(models.Model):
	user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
	post = models.ForeignKey('Post', on_delete=models.CASCADE)
	timestamp = models.DateTimeField(verbose_name='日付',default=timezone.now)

	class Meta:
		unique_together = ('user', 'post')
		ordering = ['-timestamp']

  
class Item(models.Model):
    item_name = models.CharField(verbose_name='アイテム名',blank=False,null=False,max_length=30)
    item_url_name = models.CharField(verbose_name='アイテムurl表示名',max_length=30,default=False)
    slug = models.SlugField(verbose_name="URL表示名",null=True)
    brand_name = models.CharField(verbose_name='ブランド名',max_length=20,choices = BRAND_CHOICES,default=False)
    item_photo = models.ImageField(verbose_name='アイテム画像', blank=True, null=True, upload_to='images/')
    item_position = models.CharField(verbose_name='ポジション',max_length=5,choices = RACKET_POSITION_CHOICES,default=False)
    release_date = models.DateField(verbose_name='発売月')
    display = models.BooleanField(default=False,verbose_name='表示')
  
  
  
