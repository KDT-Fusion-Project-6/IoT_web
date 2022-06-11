from datetime import datetime
from tkinter.tix import Tree
from xml.etree.ElementInclude import default_loader
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
    closet_outer_category = ( (0,'no'),(1,'Coat'), (2,'Jacket'), (3,'Jumper'), (4,'Padding'), (5,'Best'), (6,'Cardigan '), (7,'Zip-Up'))
    outer =  models.TextField(max_length=20, choices = closet_outer_category, default='0')
    closet_top_category = ( (0,'no'),(1,'Blouse'), (2,'T-shirt'), (3,'Knit'), (4,'Hoodie' ) )
    top =  models.TextField(max_length=20, choices = closet_top_category, default='0')
    closet_pants_category = ( (0,'no'),(1,'Blue jeans'), (2,'Pants'), (3,'Skirt'), (4,'Leggings'), (5,'Jogger pants') )
    pants =  models.TextField(max_length=20, choices = closet_pants_category, default='0')
    closet_onepiece_category = ((0,'no'),(1,'onepiece'),(2,'twopiece'))
    onepiece =  models.TextField(max_length=20, choices = closet_onepiece_category, default='0')

    
class Musinsa_Closet(models.Model):
    clothesId = models.IntegerField( primary_key= True )
    closet_title = models.CharField(max_length=200, default='')
    imgUrl = models.CharField(max_length=50, default='')
    closet_maincategory = ((1, 'Top'),(2,'Pants'),(3, 'Outer'),(4, 'Onepiece'))
    mainCategory =  models.TextField(max_length=20, choices = closet_maincategory, default='')
    closet_outer_category = ( (0,'no'),(1,'Coat'), (2,'Jacket'), (3,'Jumper'), (4,'Padding'), (5,'Best'), (6,'Cardigan '), (7,'Zip-Up'))
    outer =  models.TextField(max_length=20, choices = closet_outer_category, default='0')
    closet_top_category = ( (0,'no'),(1,'Blouse'), (2,'T-shirt'), (3,'Knit'), (4,'Hoodie' ) )
    top =  models.TextField(max_length=20, choices = closet_top_category, default='0')
    closet_pants_category = ( (0,'no'),(1,'Blue jeans'), (2,'Pants'), (3,'Skirt'), (4,'Leggings'), (5,'Jogger pants') )
    pants =  models.TextField(max_length=20, choices = closet_pants_category, default='0')
    closet_onepiece_category = ((0,'no'),(1,'onepiece'),(2,'twopiece'))
    onepiece =  models.TextField(max_length=20, choices = closet_onepiece_category, default='0')
    closet_style = models.CharField(max_length=100, default='')
    closet_color = models.CharField(max_length=100,default='')
    barndName = models.CharField(max_length=50, default ='' )
    ragisterDate = models.DateTimeField(max_length=200, default='')
    spring = models.BooleanField(default = True)
    summer = models.BooleanField(default = True)
    autumn = models.BooleanField(default = True)
    windter = models.BooleanField(default = True)
    elasticity = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)],default=1, null=True)
    transparency = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)],default=1, null=True)
    thickness = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)],default=1, null=True)
    texture = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)],default=1, null=True)
    price = models.IntegerField(default=1, null=True)
    regDate = models.DateField(datetime.now)

class codi_clothes(models.Model):
    cId = models.IntegerField( primary_key=True)
    codiId = models.IntegerField( default='')
    clothesId = models.ForeignKey(Musinsa_Closet, on_delete=models.CASCADE ,default='')
    
class codi(models.Model):
    codiId = models.ForeignKey(codi_clothes,on_delete=models.CASCADE, primary_key=True)
    # codiId = models.OneToOneField(codi_clothes,on_delete=models.CASCADE, primary_key=True)
    # codiId = models.ManyToManyField(codi_clothes,on_delete=models.CASCADE, primary_key=True)
    coditype = models.CharField( max_length=10, default='')
    registerDate = models.DateField(datetime.now)
    
class preferences(models.Model):
    preferences_id1= models.IntegerField( primary_key=True )
    preferences_id2 = models.ForeignKey(User, on_delete=models.CASCADE, null=True,  default= '')
    codiId = models.ForeignKey(codi,on_delete=models.CASCADE, default= '')
    ratingDate = models.DateField(datetime.now)

    
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

