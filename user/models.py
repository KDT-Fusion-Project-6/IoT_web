from django.db import models
from django.forms import ModelChoiceField

# Create your models here.
class Closet(models.Model): #옷장모델
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
    category1 =  models.CharField(max_length=2, choices = category1 )
    category2 =  models.CharField(max_length=2, choices = category2 )
    category3 =  models.CharField(max_length=2, choices = category3 )
    category4 =  models.CharField(max_length=2, choices = category4 )
class Answer(models.Model): #답변모델
    question = models.ForeignKey(Closet, on_delete=models.CASCADE) #질문 모델연결
    content = models.TextField()
    create_date = models.DateTimeField()
    
