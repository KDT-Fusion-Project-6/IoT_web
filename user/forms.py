from tkinter import Widget
from django import forms
from .models import Closet
from django.contrib.auth.models import User

class ClosetForm(forms.ModelForm):
    
    class Meta:
        model = Closet  # 사용할 모델
        fields = [
                    'closet_title',
                    'closet_uploadedFile',
                    'category1',
                    'category2',
                    'category3',
                    'category4',
                    ]  
        Widget = {
            'closet_title': forms.TextInput (attrs={'class': 'form-control'}),
        }
        labels = {
            'closet_title': '제목',
            'closet_uploadedFile': '사진 업로드',
            'category1' : '스타일',
            'category2' : '계절',
            'category3' : '핏',
            'category4' : '의류구분',
        }  
        # ClosetForm에서 사용할 Closet 모델의 속성'