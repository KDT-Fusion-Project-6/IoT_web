from django.contrib import admin
from .models import Closet

# Register your models here.

# Question모델 관리/ 검색기능
class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['subject']
    
admin.site.register(Closet, QuestionAdmin)