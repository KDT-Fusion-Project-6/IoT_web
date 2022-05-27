from django import forms
from user.models import Closet

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Closet
        fields = ['subject', 'mainphoto','content']

        widgets = {
        'subject': forms.TextInput(attrs={'class': 'form-control'}),
        'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 10}),
        }
        labels = {
        'subject': '제목',
        'mainphoto': '사진추가',
        }