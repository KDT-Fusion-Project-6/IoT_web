from time import timezone

from django.shortcuts import render
from ..models import Closet_top, Closet_pants, Closet_outer, Closet_onepiece, Closet
from django.shortcuts import render, get_object_or_404

from django.contrib.auth.decorators import login_required

from user.aws_settings import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, BUCKET_NAME, REGION
import boto3
from io  import BytesIO
from PIL import Image

from yolov5 import detect
from yolov5.cloth_style_update import extract_color
import os
import urllib
from yolov5.utils.plots import output_to_target
from django.core.files.storage import FileSystemStorage
import random

#상의등록
@login_required(login_url='login:login')
def top_closet_create(request, author_user):

    if request.method == "POST":        

        closet_top_title = request.POST["closet_top_title"]
        image = request.FILES['closet_top_uploadedFile']  # 이미지 (title.jpg)        
        user = str(request.user)    # user.id
        
        bucket_name = BUCKET_NAME
        region = REGION
        
        num = random.randrange(1, 99999)
        image_name = user + closet_top_title + str(num) +"." + image_type
        image_type = (image.content_type).split("/")[1]
        image_url = "https://"+ bucket_name + '.s3.' + region + '.amazonaws.com/' + image_name  # 업로드된 이미지의 url이 설정값으로 저장됨
        #image_url = "https://"+ bucket_name + '.s3.' + region + '.amazonaws.com/' + user +'/'+ closet_top_title +"."+image_type  # 업로드된 이미지의 url이 설정값으로 저장됨

        im = Image.open(image)   # 추가
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
        
        extract_images_info = detect.run(weights = 'yolo\\best.pt',
                        source = str(image_url),
                        #source = 'media\\images\\3.jpg',
                        data = 'yolov5\\data\\data.yaml',
                        conf_thres = 0.3,
                        line_thickness = 4,
                        project = 'media\\detect',
                        view_img = False)
        
        print(image.content_type) 
        
        items_to_list = list(extract_images_info.items())
        save_list = []
        for key, value in items_to_list: # key : 이미지 경로 value[0] 스타일 value[1] 사각형좌표
            if value:
                style = value[0]   # per image
                color, img_trim = extract_color(key, value)   # per image 
                save_list.append({'image_path':key, 'style':style, 'color':color})
            else:
                save_list.append({'image_path':key, 'style':'', 'color':''})
        print(save_list)
        
        if save_list[style] == '':
            s3_client.delete_object(Bucket=bucket_name, Key=image_name) # 이미지 삭제
            
        #if not save_list[style] :
            #pass # 비어있을경우 이미지 지우기 코드 작성
        
        else:
            im = Image.open(img_trim)   # 잘린이미지
            buffer = BytesIO()
            im.save(buffer, image_type)
            buffer.seek(0)

            s3_client.upload_fileobj(
                buffer,
                bucket_name, # 버킷이름
                image_name,
                ExtraArgs = {
                    "ContentType" : image.content_type
                }
            )
        # Saving the information in the database
            closet_top = Closet_top(
                closet_top_title = closet_top_title,
                # closet_top_url = image_url,
                closet_url = image_url,
                author = request.user,   # author_id 속성에 user.id 값 저장
                # author = author_user <-- 에러
                closet_style = save_list[style], #스타일 저장
                closet_color = save_list[color], #색 저장
            )        
            closet_top.save()    

    closet_top = Closet_top.objects.all()
    context = { "closet": closet_top }
    return render(request, "closet/closet_form_top.html", context) 

# # 디테일 페이지
# @login_required(login_url='login:login')
# def detail_top(request, author_user, closet_id):
#     Closet_top.author = author_user
#     closet = get_object_or_404(Closet_top, pk=closet_id)
#     context = {'closet': closet}
#     return render(request, 'closet/closet_detail.html', context)


#하의등록
@login_required(login_url='login:login')
def pants_closet_create(request, author_user):

    if request.method == "POST":
        
        closet_pants_title = request.POST["closet_pants_title"]
        image = request.FILES['closet_pants_uploadedFile']  # 이미지 (title.jpg)
        user = str(request.user)    # user.id
        # category_text = request.POST.get['category']
        # 1번추가        
        image_type = (image.content_type).split("/")[1]
        bucket_name = BUCKET_NAME
        region = REGION

        image_url = "https://"+ bucket_name + '.s3.' + region + '.amazonaws.com/' + user +'/'+ closet_pants_title +"."+image_type  # 업로드된 이미지의 url이 설정값으로 저장됨

        im     = Image.open(image)   # 추가
        buffer = BytesIO()
        im.save(buffer, image_type)
        buffer.seek(0)
        
        # Saving the information in the database
        closet_pants = Closet_pants(
            closet_pants_title = closet_pants_title,
            # closet_pants_url = image_url,       
            closet_url = image_url,       
            author = request.user,   # author_id 속성에 user.id 값 저장     
        #2번 추가
        )        
        closet_pants.save()

        s3_client = boto3.client(
                's3',
                aws_access_key_id = AWS_ACCESS_KEY_ID,
                aws_secret_access_key = AWS_SECRET_ACCESS_KEY
            )
        
        s3_client.upload_fileobj(
            buffer,
            bucket_name, # 버킷이름
            user +'/'+ closet_pants_title+"."+image_type,
            ExtraArgs = {
                "ContentType" : image.content_type
            }
        )

    closet_pants = Closet_pants.objects.all()
    context = { "closet": closet_pants }
    return render(request, "closet/closet_form_pants.html", context) 

# # 디테일 페이지
# @login_required(login_url='login:login')
# def detail_pants(request, author_user, closet_id):
#     Closet_pants.author = author_user
#     closet = get_object_or_404(Closet_pants, pk=closet_id)
#     context = {'closet': closet}
#     return render(request, 'closet/closet_detail.html', context)


#아우터등록
@login_required(login_url='login:login')
def outer_closet_create(request, author_user):
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
        closet_outer = Closet_outer(
            closet_outer_title = closet_outer_title,
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

    closet_outer = Closet_outer.objects.all()
    context = { "closet": closet_outer }
    return render(request, "closet/closet_form_outer.html", context) 

# # 디테일 페이지
# @login_required(login_url='login:login')
# def detail_outer(request, author_user, closet_id):
#     Closet_outer.author = author_user
#     closet = get_object_or_404(Closet_outer, pk=closet_id)
#     context = {'closet': closet}
#     return render(request, 'closet/closet_detail.html', context)


#원피스등록
@login_required(login_url='login:login')
def onepiece_closet_create(request, author_user):

    if request.method == "POST":

        closet_onepiece_title = request.POST["closet_onepiece_title"]
        image = request.FILES['closet_onepiece_uploadedFile']  # 이미지 (title.jpg)        
        user = str(request.user)    # user.id
        image_type = (image.content_type).split("/")[1]
        bucket_name = BUCKET_NAME
        region = REGION

        image_url = "https://"+ bucket_name + '.s3.' + region + '.amazonaws.com/' + user +'/'+ closet_onepiece_title +"."+image_type  # 업로드된 이미지의 url이 설정값으로 저장됨

        im     = Image.open(image)   # 추가
        buffer = BytesIO()
        im.save(buffer, image_type)
        buffer.seek(0)
        
        # Saving the information in the database
        closet_onepiece = Closet_onepiece(
            closet_onepiece_title = closet_onepiece_title,
            # closet_onepiece_url = image_url,
            closet_url = image_url,
            author = request.user,   # author_id 속성에 user.id 값 저장
        )        
        closet_onepiece.save()

        s3_client = boto3.client(
                's3',
                aws_access_key_id = AWS_ACCESS_KEY_ID,
                aws_secret_access_key = AWS_SECRET_ACCESS_KEY
            )
        
        s3_client.upload_fileobj(
            buffer,
            bucket_name, # 버킷이름
            user +'/'+ closet_onepiece_title+"."+image_type,
            ExtraArgs = {
                "ContentType" : image.content_type
            }
        )

    closet_onepiece = Closet_onepiece.objects.all()
    context = { "closet": closet_onepiece }
    return render(request, "closet/closet_form_onepiece.html", context) 

# # 디테일 페이지
# @login_required(login_url='login:login')
# def detail_onepiece(request, author_user, closet_id):
#     Closet_onepiece.author = author_user
#     closet = get_object_or_404(Closet_onepiece, pk=closet_id)
#     context = {'closet': closet}
#     return render(request, 'closet/closet_detail.html', context)