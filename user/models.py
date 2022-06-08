from tkinter.tix import Tree
from django.conf import settings
from django.db import models
from django.forms import ModelChoiceField
# from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
    # 클래스 변수 3개
    # 변수명 : 컬럼명
# class User(AbstractUser):
# followings = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="User")
    
class Closet(models.Model): #옷장모델

    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    closet_title = models.CharField(max_length=200) #제목
    closet_url = models.CharField(max_length=300) #s3 url
    closet_create_date = models.DateTimeField(auto_now = True) #날자
    closet_uploadedFile = models.ImageField(upload_to='images/', blank=True, null=True)#사진추가     
    # #카테고리 설정
    # category1 = ( ('1','1'), ('1','1'), ('1','1') )
    # category2 = ( ('1','1'), ('1','1'), ('1','1') )
    # category3 = ( ('1','1'), ('1','1'), ('1','1') )
    # category4 = ( ('1','1'), ('1','1'), ('1','1') )

    # #카테고리 실행
    # category1 =  models.TextField(max_length=20, choices = category1, default='')
    # category2 =  models.TextField(max_length=20, choices = category2, default='')
    # category3 =  models.TextField(max_length=20, choices = category3, default='')
    # category4 =  models.TextField(max_length=20, choices = category4, default='')
    
class Closet_outer(models.Model):
    # authuser = models.ForeignKey(User, on_delete=models.CASCADE, default='', null=True)

    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    closet_outer_title = models.CharField(max_length=200,default='')
    closet_outer_url = models.CharField(max_length=50, default='')
    closet_outer_uploadedFile = models.ImageField(upload_to='images/', blank=True, null=True)
    closet_outer_spring = models.BooleanField(default = True)
    closet_outer_summer = models.BooleanField(default = True)
    closet_outer_autumn = models.BooleanField(default = True)
    closet_outer_windter = models.BooleanField(default = True)
    closet_outer_color = models.CharField(max_length=100,default='')
    closet_outer_style = models.CharField(max_length=100, default='')
    closet_outer_fit = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)],default=1, null=True)
    closet_outer_category = ( ('1','1'), ('1','1'), ('1','1') )
    category1 =  models.TextField(max_length=20, choices = closet_outer_category, default='')

class Closet_top(models.Model):

    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    closet_top_title = models.CharField(max_length=200, default='')
    closet_top_url = models.CharField(max_length=50,default='')
    closet_top_uploadedFile = models.ImageField(upload_to='images/', blank=True, null=True)
    closet_top_spring = models.BooleanField(default = True)
    closet_top_summer = models.BooleanField(default = True)
    closet_top_autumn = models.BooleanField(default = True)
    closet_top_windter = models.BooleanField(default = True)
    closet_top_color = models.CharField(max_length=100,default='')
    closet_top_style = models.CharField(max_length=100, default='')
    closet_top_fit = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)],default=1, null=True)

class Closet_pants(models.Model):

    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    
    closet_pants_title = models.CharField(max_length=200, default='')
    closet_pants_url = models.CharField(max_length=50, default='')
    closet_pants_uploadedFile = models.ImageField(upload_to='images/', blank=True, null=True)
    closet_pants_spring = models.BooleanField(default = True)
    closet_pants_summer = models.BooleanField(default = True)
    closet_pants_autumn = models.BooleanField(default = True)
    closet_pants_windter = models.BooleanField(default = True)
    closet_pants_color = models.CharField(max_length=100,default='')
    closet_pants_style = models.CharField(max_length=100, default='')
    closet_pants_fit = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)],default=1, null=True)

class Closet_onepiece(models.Model):

    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    
    closet_onepiece_title = models.CharField(max_length=200, default='')
    closet_onepiece_url = models.CharField(max_length=50, default='')
    closet_onepiece_uploadedFile = models.ImageField(upload_to='images/', blank=True, null=True)
    closet_onepiece_spring = models.BooleanField(default = True)
    closet_onepiece_summer = models.BooleanField(default = True)
    closet_onepiece_autumn = models.BooleanField(default = True)
    closet_onepiece_windter = models.BooleanField(default = True)
    closet_onepiece_color = models.CharField(max_length=100,default='')
    closet_onepiece_style = models.CharField(max_length=100, default='')
    closet_onepiece_fit = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)],default=1, null=True)
    
    



