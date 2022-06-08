from time import timezone

from django.shortcuts import render
from ..models import Closet_pants
from django.shortcuts import render, get_object_or_404

from django.contrib.auth.decorators import login_required

from user.aws_settings import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, BUCKET_NAME, REGION
import boto3
from io  import BytesIO
from PIL import Image


@login_required(login_url='login:login')
def pants_closet_create(request):
#의류등록
    if request.method == "POST":
        
        closet_pants_title = request.POST["closet_pants_title"]
        image = request.FILES['closet_uploadedFile']  # 이미지 (title.jpg)
        category1 = request.POST["category1"]
        
        user = 'test-user' # 어디서? 
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
            closet_pants_url = image_url,
            category1 = category1
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

    return render(request, "closet/closet_form_pants.html", context = {
        "closet": closet_pants
    }) 