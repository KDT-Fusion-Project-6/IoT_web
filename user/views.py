from time import timezone
from urllib import request
from django.shortcuts import redirect, render, HttpResponse
from .models import Closet
from django.shortcuts import render, get_object_or_404
from datetime import datetime
from . import models
from user.aws_settings import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY
# import boto3
# from io  import BytesIO
# from PIL import Image

# Create your views here.

def index(request):
#목록출력
    page = request.GET.get('page', '1') # 페이지
    # 데이터 작성날짜 역순 조회
    closet_list = Closet.objects.order_by('-closet_create_date')
    context = {'closet_list': closet_list} 
    # closet_list.html 보여주지는 리스트
    return render(request, 'closet/closet_list.html', context)


def detail(request, closet_id):
#내용출력
    closet = get_object_or_404(Closet, pk=closet_id)
    context = {'closet': closet}
    return render(request, 'closet/closet_detail.html', context)

def closet_create(request):
#의류등록
    if request.method == "POST":
        print (request.FILES)
        closet_title = request.POST["closet_title"]
        image = request.FILES['closet_uploadedFile']  # formdata 키   
        image_time = (str(datetime.now())).replace(" ","") # 이미지이름을 시간으로 설정하기 위해 datetime를 사용
        image_type = (image.content_type).split("/")[1]
        bucket_name = "won2" #"gymin-s3"
        region = 'ca-central-1'
        im     = Image.open(image)
        buffer = BytesIO()
        im.save(buffer, image_type)
        buffer.seek(0)


        # Saving the information in the database
        closet = Closet(
            closet_title = closet_title,
            closet_uploadedFile = image
        )
        closet.save()

        # upload to S3
        s3_client = boto3.client(
                's3',
                aws_access_key_id = AWS_ACCESS_KEY_ID,
                aws_secret_access_key = AWS_SECRET_ACCESS_KEY
            )
        
        # s3_client.upload_fileobj(
        #     buffer,
        #     bucket_name, # 버킷이름
        #     closet_title+"."+image_type,
        #     # image_time+"."+image_type, # s3 저장될 파일 이름
        #     ExtraArgs = {
        #         "ContentType" : image.content_type
        #     }
        # )
        # # image_url = "http://"+ bucket_name + '.s3.' + region + '.amazonaws.com/' + image_time+"."+image_type  # 업로드된 이미지의 url이 설정값으로 저장됨
        # image_url = "http://"+ bucket_name + '.s3.' + region + '.amazonaws.com/' + closet_title+"."+image_type  # 업로드된 이미지의 url이 설정값으로 저장됨
        # # image_url = image_url.replace(" ","/")

    closet = Closet.objects.all()

    return render(request, "closet/closet_form.html", context = {
        "closet": closet
    }) 