from django.db import models
import uuid
from django.utils import timezone
from imagekit.models import ImageSpecField, ProcessedImageField
from imagekit.processors import ResizeToFill, ResizeToFit

RACKET_POSITION_CHOICES = [('後衛','後衛'),('前衛','前衛'),('前・後衛','前・後衛')] 
BRAND_CHOICES = [('YONEX','YONEX'),('MIZUNO','MIZUNO'),('DUNLOP','DUNLOP')] 
SERIES_CHOICES =[('VOLTRAGE','VOLTRAGE'),('GEOBREAK','GEOBREAK'),('F-LASER','F-LASER'),('YONEX_OTHERS','YONEX_OTHERS'),
                ('SCUD','SCUD'),('DIOS','DIOS'),('MIZUNO_OTHERS','MIZUNO_OTHERS'),
                ('GALAXEED','GALAXEED'),('JETSTORM','JETSTORM'),('DUNLOP_OTHERS','DUNLOP_OTHERS')]


class Post(models.Model):
        id = models.UUIDField(default=uuid.uuid4,primary_key=True, editable=False)
        author = models.ForeignKey('accounts.CustomUser', on_delete=models.CASCADE)
        item = models.ForeignKey('timeline.Item', on_delete=models.CASCADE)
        text = models.TextField(verbose_name='本文',max_length=200,)
        photo = models.ImageField(verbose_name='写真', blank=True, null=True, upload_to='images/')
        post_photo = ImageSpecField(source='photo',processors=[ResizeToFit(1080, 1080)],format='JPEG',options={'quality':60})
        created_at = models.DateTimeField(default=timezone.now)
        edited = models.BooleanField(default=False,verbose_name='編集済み')

        def __str__(self):
            return f"{self.author.username} {self.item.item_name}"

        class Meta:
            ordering = ['-created_at']


class Like(models.Model):
        id = models.UUIDField(default=uuid.uuid4,primary_key=True, editable=False)
        user = models.ForeignKey('accounts.CustomUser', on_delete=models.CASCADE)
        post = models.ForeignKey('Post', on_delete=models.CASCADE)
        timestamp = models.DateTimeField(verbose_name='日付',default=timezone.now)

        class Meta:
                unique_together = ('user', 'post')
                ordering = ['-timestamp']

  
class Item(models.Model):
    item_name = models.CharField(verbose_name='アイテム名',blank=False,null=False,max_length=30)
    slug = models.SlugField(verbose_name="URL表示名",max_length=30,null=True)
    brand_name = models.CharField(verbose_name='ブランド名',max_length=20,choices = BRAND_CHOICES,default=False)
    series_name = models.CharField(verbose_name='シリーズ名',max_length=20,choices = SERIES_CHOICES,default=False)
    item_photo = models.ImageField(verbose_name='アイテム画像', blank=True, null=True, upload_to='images/')
    item_position = models.CharField(verbose_name='ポジション',max_length=5,choices = RACKET_POSITION_CHOICES,default=False)
    release_date = models.DateField(verbose_name='発売月')
    display = models.BooleanField(default=False,verbose_name='表示')

    def __str__(self):
            return f"{self.pk} {self.item_name}"

    class Meta:
	    ordering = ['-release_date']
