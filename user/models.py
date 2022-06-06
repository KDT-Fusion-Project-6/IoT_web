from django.db import models
from django.forms import ModelChoiceField
from django.contrib.auth.models import User
# Create your models here.
class Closet(models.Model): #옷장모델
    auth_user = models.ForeignKey(User, on_delete=models.CASCADE)
    closet_title = models.CharField(max_length=200) #제목
    closet_url = models.CharField(max_length=300) #s3 url
    closet_content = models.TextField() #내용
    closet_create_date = models.DateTimeField(auto_now = True) #날자
    closet_uploadedFile = models.ImageField(upload_to='images/', blank=True, null=True)#사진추가     
    #카테고리 설정
    category1 = ( ('1','1'), ('1','1'), ('1','1') )
    category2 = ( ('1','1'), ('1','1'), ('1','1') )
    category3 = ( ('1','1'), ('1','1'), ('1','1') )
    category4 = ( ('1','1'), ('1','1'), ('1','1') )

    #카테고리 실행
    category1 =  models.CharField(max_length=2, choices = category1, default='')
    category2 =  models.CharField(max_length=2, choices = category2, default='')
    category3 =  models.CharField(max_length=2, choices = category3, default='')
    category4 =  models.CharField(max_length=2, choices = category4, default='')
    
class Answer(models.Model): #답변모델
    question = models.ForeignKey(Closet, on_delete=models.CASCADE) #질문 모델연결
    content = models.TextField()
    create_date = models.DateTimeField()
    
