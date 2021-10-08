from django.db import models
from django.utils import timezone
from imagekit.models import ImageSpecField, ProcessedImageField
from imagekit.processors import ResizeToFill, ResizeToFit
from django.contrib.auth import get_user_model
from django.contrib.sessions.models import Session

RACKET_POSITION_CHOICES = [('後衛','後衛'),('前衛','前衛'),('両用','両用')] 
BRAND_CHOICES = [('YONEX','YONEX'),('MIZUNO','MIZUNO'),('DUNLOP','DUNLOP'),('GOSEN','GOSEN'),('SRIXON','SRIXON')] 

CustomUser = get_user_model()

class Post(models.Model):
	author = models.ForeignKey('accounts.CustomUser', on_delete=models.CASCADE)
	product_id = models.ForeignKey('timeline.ProductModel', on_delete=models.CASCADE)
	slug = models.SlugField(verbose_name="URLスラッグ（英語）",null=True)
	text = models.TextField(verbose_name='本文',max_length=200, blank=True, null=True)
	photo = models.ImageField(verbose_name='写真', blank=True, null=True, upload_to='images/')
	post_photo = ImageSpecField(source='photo',processors=[ResizeToFit(1080, 1080)],format='JPEG',options={'quality':60})
	created_at = models.DateTimeField(auto_now_add=True)
	#必要に応じてlike数を上下させるカラムを追加する
	class Meta:
    		ordering = ['-created_at']
 
class Like(models.Model):
	user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
	post = models.ForeignKey('Post', on_delete=models.CASCADE)
	timestamp = models.DateTimeField(default=timezone.now)

	class Meta:
		unique_together = ('user', 'post')

  
class ProductModel(models.Model):
    racket_name = models.CharField(verbose_name='ラケット名',max_length=30)
    racket_url_name = models.CharField(verbose_name='ラケットurl表示名',max_length=30)
    slug = models.SlugField(verbose_name="URLスラッグ（英語）",null=True)
    brand = models.CharField(verbose_name='ブランド',max_length=30,choices = BRAND_CHOICES)
    racket_photo = models.ImageField(verbose_name='ラケット写真', blank=True, null=True, upload_to='images/')
    recommend_position = models.CharField(verbose_name='ポジション',max_length=5,choices = RACKET_POSITION_CHOICES)
    release_date = models.DateField(verbose_name='発売日')
  
  
  
