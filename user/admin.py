from django.contrib import admin
from .models import Closet, Musinsa_Closet, preferences, codi_clothes, codi

# Register your models here.

# Question모델 관리/ 검색기능
class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['closet_title']
    
admin.site.register(Closet, QuestionAdmin)
admin.site.register(Musinsa_Closet, QuestionAdmin)
admin.site.register(preferences, QuestionAdmin)
admin.site.register(codi_clothes, QuestionAdmin)
admin.site.register(codi, QuestionAdmin)
