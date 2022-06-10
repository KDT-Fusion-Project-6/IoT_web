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


# 디테일 페이지
@login_required(login_url='login:login')
def detail(request, author_user, closet_id):
    Closet.author = author_user
    closet = get_object_or_404(Closet, pk=closet_id)
    context = {'closet': closet}
    return render(request, 'closet/closet_detail.html', context)


#아우터등록
@login_required(login_url='login:login')
def closet_create(request, author_user):
    if request.method == "POST":
        # print(request)
        closet_outer_title = request.POST["closet_title"]       

        image = request.FILES['closet_uploadedFile']  # 이미지 (title.jpg)
        
        # section = request.POST["section"]
        section = "3"
        outer = request.POST["outer"]
        # top = request.POST["top"]
        # pants = request.POST["pants"]
        # onepiece = request.POST["onepiece"]
        
        closet_spring = request.POST.get('closet_spring',False)
        if closet_spring == "on":
            closet_spring = True
        
        closet_summer = request.POST.get('closet_summer',False)
        if closet_summer == "on":
            closet_summer = True
            
        closet_fall = request.POST.get('closet_fall',False)
        if closet_fall == "on":
            closet_fall = True
            
        closet_winter = request.POST.get('closet_winter',False)
        if closet_winter == "on":
            closet_winter = True

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

            section = section, 
            outer = outer, 
            # top = top, 
            # pants = pants, 
            # onepiece = onepiece, 
            
            closet_spring = closet_spring,
            closet_summer = closet_summer,
            closet_fall = closet_fall,
            closet_winter = closet_winter,
        )    

        closet_outer.save()
        print(closet_outer)
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