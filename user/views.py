from multiprocessing import context
from time import timezone
from urllib import request
from django.shortcuts import redirect, render, HttpResponse
from .models import Closet
from django.shortcuts import render, get_object_or_404
from .froms import QuestionForm
from datetime import datetime

# Create your views here.

def index(request):
    """
    closet 목록 출력
    """
    page = request.GET.get('page', '1') # 페이지
    # 데이터 작성날짜 역순 조회
    closet_list = Closet.objects.order_by('-create_date')
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
    """
    closet 의류등록
    """
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.create_date = datetime.now()
            question.save()
            return redirect('closet:index')
    else:
        form = QuestionForm()
    context = {'form': form}
    return render(request, 'closet/closet_form.html', context)    
    
    
    # """
    # pybo 옷장 등록
    # """
    # form = QuestionForm()
    # return render(request, 'closet/closet_form.html', {'form': form})