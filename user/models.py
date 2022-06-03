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
    category1 = ( ('1','스키니'), ('2','슬림'), ('3','레귤러'), ('4','루즈'), ('5','오버사이즈') )
    category2 = ( ('1','봄'), ('2','여름'), ('3','가을'), ('4','겨울') )
    category3 = ( ('1','트래디셔널'), ('2','매니시'), ('3','페미닌') ,('4','에스닉'), ('5','컨템포러리'), ('6','내추럴'), ('7','젠더플루이드'), ('8','스포티'), ('9','서브컬쳐'), ('10','캐주얼') )
    category4 = ( ('1','상의'), ('2','하의'), ('3','아우터') )
    
    #카테고리 실행
    category1 =  models.CharField(max_length=2, choices = category1, default='')
    category2 =  models.CharField(max_length=2, choices = category2, default='')
    category3 =  models.CharField(max_length=2, choices = category3, default='')
    category4 =  models.CharField(max_length=2, choices = category4, default='')
    
class Answer(models.Model): #답변모델
    question = models.ForeignKey(Closet, on_delete=models.CASCADE) #질문 모델연결
    content = models.TextField()
    create_date = models.DateTimeField()
    
