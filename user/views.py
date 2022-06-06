from time import timezone

from django.shortcuts import render
from .models import Closet
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
def closet_create(request): #상의 
#의류등록
    if request.method == "POST":
        closet_title = request.POST["closet_title"]
        image = request.FILES['closet_uploadedFile']  # 이미지 (title.jpg)
        user = 'test-user' # 어디서? 
        print('----------------------------------------------------')
        print(image)   
          
        bucket_name = BUCKET_NAME
        region = REGION
        #image_type = "jpg"
        num = random.randrange(1, 99999)
        image_type = (image.content_type).split("/")[1]
        image_name = user +'/top-'+ str(num) +"." + image_type
        image_url = "https://"+ bucket_name + '.s3.' + region + '.amazonaws.com/' + image_name  # 업로드된 이미지의 url이 설정값으로 저장됨
        # image_url = ""
        print(image_url)
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
        
        #
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
        
            closet = Closet(
                closet_title = closet_title,
                closet_url = image_url,
                closet_style = save_list[style], #스타일 저장
                closet_color = save_list[color] #색 저장
            )
            closet.save()
        
        #print('----------------------------------------------------')
        
        # Saving the information in the database

    closet = Closet.objects.all()

    return render(request, "closet/closet_form.html", context = {
        "closet": closet
    }) 
"""  
# 장고와 욜로 모델 연결부분 추가필요    
from yolov5 import detect
import os
import urllib
from yolov5.utils.plots import output_to_target
from django.core.files.storage import FileSystemStorage

async def predictImage(request):
    print(request)
    print(request.POST.dict())
    fileObj = request.FILES['filePath']
    fs=FileSystemStorage()
    filePathName= fs.save(fileObj.name, fileObj)
    filePathName = fs.url(filePathName)
    filename = os.path.basename(filePathName.replace('%20',''))
    result = detect.run(weights = 'yolo/best.pt',
                        source = image_url,
                        conf_thres = 0.3,
                        line_thickness = 4,
                        imgsz = [640,640],
                        project = 'media/detect',
                        view_img = False) 
    detect.parse_opt()
    last = detect.main()
    # 여기서 나오는 두개의 결과를 closet DB에 넣으면 될 것 같음 
    # closet_style = last[1]  , closet_color = last[2] 
    output='media/detect/'+os.path.basename(filePathName)
    context={'filePathName':filePathName, 'output': output, 'result':result}
    return render(request, '~~~.html', context)"""