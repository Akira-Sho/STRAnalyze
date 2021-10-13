from django.db import models
from django.contrib.auth.models import AbstractUser
from imagekit.models import ImageSpecField, ProcessedImageField
from imagekit.processors import ResizeToFill
from django.core.validators import MaxValueValidator

AGE_CHOICES = [('12歳以下','12歳以下'),('13歳','13歳'),('14歳','14歳'),('15歳','15歳'),('16歳','16歳'),('17歳','17歳'),('18歳','18歳'),('19歳~20歳','19歳~20歳'),('21歳~22歳','21歳~22歳'),('23歳~25歳','23歳~25歳'),('26歳~29歳','26歳~29歳'),('30歳~39歳','30歳~39歳'),('40歳~49歳','40歳~49歳'),('50歳~59歳','50歳~59歳'),('60歳~69歳','60歳~69歳'),('70歳以上','70歳以上')]
HISTORY_CHOICES = [('1年未満', '1年未満'), ('1年以上3年未満', '1年以上3年未満'), ('3年以上6年未満', '3年以上6年未満'), ('6年以上8年未満', '6年以上8年未満'), ('8年以上10年未満', '8年以上10年未満'), ('10年以上', '10年以上')]
GENDER_CHOICES = [('男性', '男性'), ('女性', '女性')]
AREA_CHOICES = [('北海道', '北海道'), ('東北', '東北'), ('関東', '関東'), ('中部', '中部'), ('近畿', '近畿'), ('中国', '中国'), ('四国', '四国'), ('九州', '九州'), ('その他', 'その他')]
POSITION_CHOICES = [('後衛','後衛'),('前衛','前衛')] 



class CustomUser(AbstractUser):
    email = models.EmailField(verbose_name='メールアドレス')
    description = models.TextField(verbose_name='プロフィール', max_length=120, null=True, blank=True)
    photo = models.ImageField(verbose_name='写真', blank=True, null=True, upload_to='images/')
    thumbnail = ImageSpecField(source='photo',
                               processors=[ResizeToFill(256, 256)],
                               format='JPEG',
                               options={'quality': 60})

    age = models.CharField(max_length=30,verbose_name='年齢',choices = AGE_CHOICES,null=True, blank=True)
    gender = models.CharField(max_length=15, verbose_name='性別',choices = GENDER_CHOICES,null=True, blank=True)
    
    history = models.CharField(max_length=25, verbose_name='競技経験年数',choices = HISTORY_CHOICES,null=True, blank=True)
    
    activity_area = models.CharField(max_length=5, verbose_name='活動エリア',choices = AREA_CHOICES,null=True, blank=True)
    position = models.CharField(max_length=5, verbose_name='ポジション',choices = POSITION_CHOICES,null=True, blank=True)
    
    class Meta:
        verbose_name_plural = 'CustomUser'


