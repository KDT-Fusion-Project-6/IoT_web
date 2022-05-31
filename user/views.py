from time import timezone
from urllib import request
from django.shortcuts import redirect, render, HttpResponse
from .models import Closet
from django.shortcuts import render, get_object_or_404
from datetime import datetime
from . import models
# Create your views here.

def index(request):
    """
    closet 목록 출력
    """
    page = request.GET.get('page', '1') # 페이지
    # 데이터 작성날짜 역순 조회
    closet_list = Closet.objects.order_by('-closet_create_date')
    context = {'closet_list': closet_list} 
    # closet_list.html 보여주지는 리스트
    return render(request, 'closet/closet_list.html', context)


def detail(request, closet_id):
    """
    closet 내용 출력
    """
    question = get_object_or_404(Closet, pk=closet_id)
    context = {'question': question}
    return render(request, 'closet/closet_detail.html', context)



def closet_create(request):
    #의류등록
    if request.method == "POST":
        # Fetching the form data
        closet_title = request.POST["closet_title"]
        closet_uploadedFile = request.FILES["closet_uploadedFile"]

        # Saving the information in the database
        closet = Closet(
            closet_title = closet_title,
            closet_uploadedFile = closet_uploadedFile
        )
        closet.save()

    closet = Closet.objects.all()

    return render(request, "closet/closet_form.html", context = {
        "closet": closet
    })