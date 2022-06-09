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

    closet_spring = models.BooleanField(default = True)
    closet_summer = models.BooleanField(default = True)
    closet_fall = models.BooleanField(default = True)
    closet_winter = models.BooleanField(default = True)

    closet_color = models.CharField(max_length=100,default='')
    closet_style = models.CharField(max_length=100, default='')
    closet_fit = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)],default=1, null=True)

    closet_section_category = ((1, 'Top'),(2,'Pants'),(3, 'Outer'),(4, 'Onepiece'))
    section =  models.TextField(max_length=20, choices = closet_section_category, default='')
    
    closet_outer_category = ( (1,'Coat'), (2,'Jacket'), (3,'Jumper'), (4,'Padding'), (5,'Best'), (6,'Cardigan '), (7,'Zip-Up'))
    outer =  models.TextField(max_length=20, choices = closet_outer_category, default='')
    
    closet_top_category = ( (1,'Blouse'), (2,'T-shirt'), (3,'Knit'), (4,'Hoodie' ) )
    top =  models.TextField(max_length=20, choices = closet_top_category, default='')
    
    closet_pants_category = ( (1,'Blue jeans'), (2,'Pants'), (3,'Skirt'), (4,'Leggings'), (5,'Jogger pants') )
    pants =  models.TextField(max_length=20, choices = closet_pants_category, default='')
    
    closet_onepiece_category = ((1,'onepiece'),(2,'twopiece'))
    onepiece =  models.TextField(max_length=20, choices = closet_onepiece_category, default='')


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
    
# class Closet_outer(models.Model):
#     # authuser = models.ForeignKey(User, on_delete=models.CASCADE, default='', null=True)

#     author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

#     closet_outer_title = models.CharField(max_length=200,default='')
#     # closet_outer_url = models.CharField(max_length=50, default='')
#     closet_url = models.CharField(max_length=50, default='')
#     closet_outer_uploadedFile = models.ImageField(upload_to='images/', blank=True, null=True)
#     closet_outer_spring = models.BooleanField(default = True)
#     closet_outer_summer = models.BooleanField(default = True)
#     closet_outer_autumn = models.BooleanField(default = True)
#     closet_outer_windter = models.BooleanField(default = True)
#     closet_outer_color = models.CharField(max_length=100,default='')
#     closet_outer_style = models.CharField(max_length=100, default='')
#     closet_outer_fit = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)],default=1, null=True)
#     closet_outer_category = ( ('1','1'), ('1','1'), ('1','1') )
#     category1 =  models.TextField(max_length=20, choices = closet_outer_category, default='')

# class Closet_top(models.Model):

#     author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

#     closet_top_title = models.CharField(max_length=200, default='')
#     # closet_top_url = models.CharField(max_length=50,default='')
#     closet_url = models.CharField(max_length=50,default='')
#     closet_top_uploadedFile = models.ImageField(upload_to='images/', blank=True, null=True)
#     closet_top_spring = models.BooleanField(default = True)
#     closet_top_summer = models.BooleanField(default = True)
#     closet_top_autumn = models.BooleanField(default = True)
#     closet_top_windter = models.BooleanField(default = True)
#     closet_top_color = models.CharField(max_length=100,default='')
#     closet_top_style = models.CharField(max_length=100, default='')
#     closet_top_fit = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)],default=1, null=True)

# class Closet_pants(models.Model):

#     author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    
#     closet_title = models.CharField(max_length=200, default='')
#     # closet_url = models.CharField(max_length=50, default='')
#     closet_url = models.CharField(max_length=50, default='')
#     closet_uploadedFile = models.ImageField(upload_to='images/', blank=True, null=True)
#     closet_spring = models.BooleanField(default = True)
#     closet_summer = models.BooleanField(default = True)
#     closet_autumn = models.BooleanField(default = True)
#     closet_windter = models.BooleanField(default = True)
#     closet_color = models.CharField(max_length=100,default='')
#     closet_style = models.CharField(max_length=100, default='')
#     closet_fit = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)],default=1, null=True)

# class Closet_onepiece(models.Model):

#     author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    
#     closet_onepiece_title = models.CharField(max_length=200, default='')
#     # closet_onepiece_url = models.CharField(max_length=50, default='')
#     closet_url = models.CharField(max_length=50, default='')
#     closet_onepiece_uploadedFile = models.ImageField(upload_to='images/', blank=True, null=True)
#     closet_onepiece_spring = models.BooleanField(default = True)
#     closet_onepiece_summer = models.BooleanField(default = True)
#     closet_onepiece_autumn = models.BooleanField(default = True)
#     closet_onepiece_windter = models.BooleanField(default = True)
#     closet_onepiece_color = models.CharField(max_length=100,default='')
#     closet_onepiece_style = models.CharField(max_length=100, default='')
#     closet_onepiece_fit = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)],default=1, null=True)
    
    



