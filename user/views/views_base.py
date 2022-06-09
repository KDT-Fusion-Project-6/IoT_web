from time import timezone

from django.shortcuts import render
from ..models import Closet
from django.shortcuts import render, get_object_or_404

from django.contrib.auth.decorators import login_required

from user.aws_settings import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, BUCKET_NAME, REGION
import boto3
from io  import BytesIO
from PIL import Image


# @login_required(login_url='login:login')
# def index(request):
# #목록출력
#     page = request.GET.get('page', '1') # 페이지
#     # 데이터 작성날짜 역순 조회
#     closet_list = Closet.objects.order_by('-closet_create_date') # 날짜

#     context = {'closet_list': closet_list} 
#     # print (context)
#     # closet_list.html 보여주지는 리스트
#     return render(request, 'closet_list.html', context)


# 유저별 목록
@login_required(login_url='login:login')
def author_closet(request, author_id):
    
    page = request.GET.get('page', '1') # 페이지
    # 데이터 작성날짜 역순 조회
    closet_list = Closet.objects.filter(author=author_id).order_by('-closet_create_date') # 날짜

    context = {'closet_list': closet_list}    
    return render(request, 'closet_list.html', context)
    

# 디테일 페이지
@login_required(login_url='login:login')
def detail(request, author_user, closet_id):
    Closet.author = author_user
    closet = get_object_or_404(Closet, pk=closet_id)
    context = {'closet': closet}
    return render(request, 'closet/closet_detail.html', context)

# @login_required(login_url='login:login')
# def detail_top(request, author_user, closet_id):
#     Closet.author = author_user
#     closet = get_object_or_404(Closet, pk=closet_id)
#     context = {'closet': closet}
#     return render(request, 'closet/closet_detail_top.html', context)

# @login_required(login_url='login:login')
# def detail_pants(request, author_user, closet_id):
#     Closet.author = author_user
#     closet = get_object_or_404(Closet, pk=closet_id)
#     context = {'closet': closet}
#     return render(request, 'closet/closet_detail_pants.html', context)

# @login_required(login_url='login:login')
# def detail_outer(request, author_user, closet_id):
#     Closet.author = author_user
#     closet = get_object_or_404(Closet, pk=closet_id)
#     context = {'closet': closet}
#     return render(request, 'closet/closet_detail_outer.html', context)

# @login_required(login_url='login:login')
# def detail_onepiece(request, author_user, closet_id):
#     Closet.author = author_user
#     closet = get_object_or_404(Closet, pk=closet_id)
#     context = {'closet': closet}
#     return render(request, 'closet/closet_detail_.html', context)


# @login_required(login_url='login:login')
# def closet_create(request):
# #의류등록
#     if request.method == "POST":
        
#         closet_title = request.POST["closet_title"]
#         image = request.FILES['closet_uploadedFile']  # 이미지 (title.jpg)
#         category1 = request.POST["category1"]
        
#         user = 'test-user' # 어디서? 
#         image_type = (image.content_type).split("/")[1]
#         bucket_name = BUCKET_NAME
#         region = REGION

#         image_url = "https://"+ bucket_name + '.s3.' + region + '.amazonaws.com/' + user +'/'+ closet_title +"."+image_type  # 업로드된 이미지의 url이 설정값으로 저장됨

#         im     = Image.open(image)   # 추가
#         buffer = BytesIO()
#         im.save(buffer, image_type)
#         buffer.seek(0)
        
#         # Saving the information in the database
#         closet = Closet(
#             closet_title = closet_title,
#             closet_url = image_url,
#             category1 = category1
#         )
        
#         closet.save()

#         s3_client = boto3.client(
#                 's3',
#                 aws_access_key_id = AWS_ACCESS_KEY_ID,
#                 aws_secret_access_key = AWS_SECRET_ACCESS_KEY
#             )
        
#         s3_client.upload_fileobj(
#             buffer,
#             bucket_name, # 버킷이름
#             user +'/'+ closet_title+"."+image_type,
#             ExtraArgs = {
#                 "ContentType" : image.content_type
#             }
#         )

#     closet = Closet.objects.all()

#     return render(request, "closet/closet_form.html", context = {
#         "closet": closet
#     }) 