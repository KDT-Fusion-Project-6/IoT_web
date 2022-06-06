from time import timezone

from django.shortcuts import render
from .models import Closet
from django.shortcuts import render, get_object_or_404

from django.contrib.auth.decorators import login_required

from user.aws_settings import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, BUCKET_NAME, REGION
import boto3
from io  import BytesIO
from PIL import Image
import random

@login_required(login_url='login:login')
def index(request):
#목록출력
    page = request.GET.get('page', '1') # 페이지
    # 데이터 작성날짜 역순 조회
    closet_list = Closet.objects.order_by('-closet_create_date') # 날짜

    context = {'closet_list': closet_list} 
    # print (context)
    # closet_list.html 보여주지는 리스트
    return render(request, 'closet/closet_list.html', context)


@login_required(login_url='login:login')
def detail(request, closet_id):
#내용출력
    closet = get_object_or_404(Closet, pk=closet_id)
    context = {'closet': closet}
    return render(request, 'closet/closet_detail.html', context)


@login_required(login_url='login:login')
def closet_create(request):
#의류등록
    if request.method == "POST":
        closet_title = request.POST["closet_title"]
        image = request.FILES['closet_uploadedFile']  # 이미지 (title.jpg)
        user = 'test-user' # 어디서? 

        image_type = (image.content_type).split("/")[1]
        bucket_name = BUCKET_NAME
        region = REGION
        num = random.randrange(1, 99999)
        image_name = user +'/top-'+ str(num) +"." + image_type
        image_url = "https://"+ bucket_name + '.s3.' + region + '.amazonaws.com/' + image_name  # 업로드된 이미지의 url이 설정값으로 저장됨

        im     = Image.open(image)   # 추가
        buffer = BytesIO()
        im.save(buffer, image_type)
        buffer.seek(0)
    
        s3_client = boto3.client(
                's3',
                aws_access_key_id = AWS_ACCESS_KEY_ID,
                aws_secret_access_key = AWS_SECRET_ACCESS_KEY
            )
        
        s3_client.upload_fileobj(
            buffer,
            bucket_name, # 버킷이름
            image_name,
            ExtraArgs = {
                "ContentType" : image.content_type
            }
        )

        # Saving the information in the database
        closet = Closet(
            closet_title = closet_title,
            closet_url = image_url
        )
        closet.save()

        s3_client.delete_object(Bucket=bucket_name, Key=image_name) # 이미지 삭제

    closet = Closet.objects.all()

    return render(request, "closet/closet_form.html", context = {
        "closet": closet
    }) 