from time import timezone

from django.shortcuts import render
from django.urls import is_valid_path
from ..models import Closet
from django.shortcuts import render, get_object_or_404

from django.contrib.auth.decorators import login_required

from user.aws_settings import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, BUCKET_NAME, REGION
import boto3
from io  import BytesIO
from PIL import Image



#아우터등록
@login_required(login_url='login:login')
def closet_create(request, author_user):
    if request.method == "POST":
        # print(request)
        closet_outer_title = request.POST["closet_outer_title"]
        image = request.FILES['closet_outer_uploadedFile']  # 이미지 (title.jpg)
        user = str(request.user)    # user.id        
        image_type = (image.content_type).split("/")[1]
        bucket_name = BUCKET_NAME
        region = REGION

        image_url = "https://"+ bucket_name + '.s3.' + region + '.amazonaws.com/' + user +'/'+ closet_outer_title +"."+image_type  # 업로드된 이미지의 url이 설정값으로 저장됨

        im     = Image.open(image)   # 추가
        buffer = BytesIO()
        im.save(buffer, image_type)
        buffer.seek(0)
        
        # Saving the information in the database
        closet_outer = Closet(
            closet_title = closet_outer_title,
            # closet_outer_url = image_url,
            closet_url = image_url,
            author = request.user,   # author_id 속성에 user.id 값 저장
        )      
        closet_outer.save()

        s3_client = boto3.client(
                's3',
                aws_access_key_id = AWS_ACCESS_KEY_ID,
                aws_secret_access_key = AWS_SECRET_ACCESS_KEY
            )
        
        s3_client.upload_fileobj(
            buffer,
            bucket_name, # 버킷이름
            user +'/'+ closet_outer_title+"."+image_type,
            ExtraArgs = {
                "ContentType" : image.content_type
            }
        )

    closet_outer = Closet.objects.all()
    context = { "closet": closet_outer }
    return render(request, "closet/closet_form_outer.html", context) 

# # 디테일 페이지
# @login_required(login_url='login:login')
# def detail_outer(request, author_user, closet_id):
#     Closet_outer.author = author_user
#     closet = get_object_or_404(Closet_outer, pk=closet_id)
#     context = {'closet': closet}
#     return render(request, 'closet/closet_detail.html', context)