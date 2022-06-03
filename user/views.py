from multiprocessing import context
from time import timezone
from urllib import request
from django.shortcuts import redirect, render, HttpResponse

from user.forms import ClosetForm
from .models import Closet
from django.shortcuts import render, get_object_or_404
from datetime import datetime
from . import models
from user.aws_settings import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, BUCKET_NAME, REGION
import boto3
from io  import BytesIO
from PIL import Image

# Create your views here.

def index(request):
#목록출력
    page = request.GET.get('page', '1') # 페이지
    # 데이터 작성날짜 역순 조회
    closet_list = Closet.objects.order_by('-closet_create_date') # 날짜

    context = {'closet_list': closet_list} 
    # print (context)
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
        #     closet_title = request.POST["closet_title"]
    #     image = request.FILES['closet_uploadedFile']  # 이미지 (title.jpg)
        form = ClosetForm(request.POST)
        if form.is_valid(): # 폼이 유효하면
            closet = form.save(commit=False) # 임시저장해서 closet 객체 리턴
            closet.save() # 데이터 저장
            return redirect('closet:index')
        
    form = ClosetForm()
    context = {'form':form}

    return render(request, "closet/closet_form.html", context)