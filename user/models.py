from django.db import models

# Create your models here.
class Closet(models.Model): #옷장모델
    subject = models.CharField(max_length=200) #제목
    content = models.TextField() #내용
    create_date = models.DateTimeField() #날자
    mainphoto = models.ImageField(upload_to='images/', blank=True, null=True)#사진추가

class Answer(models.Model): #답변모델
    question = models.ForeignKey(Closet, on_delete=models.CASCADE) #질문 모델연결
    content = models.TextField()
    create_date = models.DateTimeField()