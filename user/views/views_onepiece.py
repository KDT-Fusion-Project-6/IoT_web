from time import timezone

from django.shortcuts import render
from ..models import Closet
from django.shortcuts import render, get_object_or_404


from django.contrib.auth.decorators import login_required

from user.aws_settings import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, BUCKET_NAME, REGION
import boto3
from io  import BytesIO
from PIL import Image



#원피스등록
@login_required(login_url='login:login')
def closet_create(request, author_user):

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
        closet_onepiece = Closet(
            closet_title = closet_onepiece_title,
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
    
    closet_onepiece = Closet.objects.all()
    context = { "closet": closet_onepiece }
    return render(request, "closet/closet_form_onepiece.html", context) 

# # 디테일 페이지
# @login_required(login_url='login:login')
# def detail_onepiece(request, author_user, closet_id):
#     Closet_onepiece.author = author_user
#     closet = get_object_or_404(Closet_onepiece, pk=closet_id)
#     context = {'closet': closet}
#     return render(request, 'closet/closet_detail.html', context)