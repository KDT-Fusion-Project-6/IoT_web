from django.conf import settings
from django.db import models
from django.forms import ModelChoiceField
# from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User

# Create your models here.
    # 클래스 변수 3개
    # 변수명 : 컬럼명
# class User(AbstractUser):
# followings = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="User")
    
class Closet(models.Model): #옷장모델
    auth_user = models.ForeignKey(User, on_delete=models.CASCADE)
    closet_title = models.CharField(max_length=200, default='') #제목
    closet_url = models.CharField(max_length=300, default='') #s3 url
    closet_create_date = models.DateTimeField(auto_now = True) #날자
    closet_uploadedFile = models.ImageField(upload_to='images/', blank=True, null=True)#사진추가     
    #카테고리 설정
    category1 = ( ('1','1'), ('1','1'), ('1','1') )
    category2 = ( ('1','1'), ('1','1'), ('1','1') )
    category3 = ( ('1','1'), ('1','1'), ('1','1') )
    category4 = ( ('1','1'), ('1','1'), ('1','1') )

    #카테고리 실행
    category1 =  models.TextField(max_length=20, choices = category1, default='')
    category2 =  models.TextField(max_length=20, choices = category2, default='')
    category3 =  models.TextField(max_length=20, choices = category3, default='')
    category4 =  models.TextField(max_length=20, choices = category4, default='')
    
class Closet_outer(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    closet_outer_title = models.CharField(max_length=200,default='')
    closet_outer_url = models.CharField(max_length=50, default='')
    closet_outer_uploadedFile = models.ImageField(upload_to='images/closet_outer', blank=True, null=True)
    category1 = models.BooleanField(default = True)
    category2 = models.BooleanField(default = True)
    category3 = models.BooleanField(default = True)
    category4 = models.BooleanField(default = True)

class Closet_top(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    closet_top_title = models.CharField(max_length=200, default='')
    closet_top_url = models.CharField(max_length=50,default='')
    closet_top_uploadedFile = models.ImageField(upload_to='images/closet_top', blank=True, null=True)
    category1 = models.BooleanField(default = True)
    category2 = models.BooleanField(default = True)
    category3 = models.BooleanField(default = True)
    category4 = models.BooleanField(default = True)
    
class Closet_pants(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    closet_pants_title = models.CharField(max_length=200, default='')
    closet_pants_url = models.CharField(max_length=50, default='')
    closet_pants_uploadedFile = models.ImageField(upload_to='images/closet_pants', blank=True, null=True)
    category1 = models.BooleanField(default = True)
    category2 = models.BooleanField(default = True)
    category3 = models.BooleanField(default = True)
    category4 = models.BooleanField(default = True)

class Closet_onepiece(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    closet_onepiece_title = models.CharField(max_length=200, default='')
    closet_onepiece_url = models.CharField(max_length=50, default='')
    closet_onepiece_uploadedFile = models.ImageField(upload_to='images/closet_onepiece', blank=True, null=True)
    category1 = models.BooleanField(default = True)
    category2 = models.BooleanField(default = True)
    category3 = models.BooleanField(default = True)
    category4 = models.BooleanField(default = True)
