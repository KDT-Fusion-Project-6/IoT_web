from django.urls import path
from .views import views_outer, views_pants, views_top, views_onepiece, views_base
from django.conf.urls.static import static
from django.conf import settings

app_name = 'closet'

urlpatterns = [
    
    # path('', views_base.index, name='index'),
    path('<int:author_id>/', 
    views_base.author_closet, name='author_closet'),

    # 옷장 보여주기
    path('<int:author_user>/<int:closet_id>/', 
    views_base.detail, name ='detail'),

    # path('<int:author_user>/<int:closet_id>/', 
    # views_base.detail_top, name ='detail_top'),

    # path('<int:author_user>/<int:closet_id>/', 
    # views_base.detail_pants, name ='detail_pants'),

    # path('<int:author_user>/<int:closet_id>/', 
    # views_base.detail_outer, name ='detail_outer'),

    # path('<int:author_user>/<int:closet_id>/', 
    # views_base.detail_onepiece, name ='detail_onepiece'),

    
    # 상의
    path('closet/top_create/<int:author_user>/', 
    views_top.closet_create, name='top_create'), # 등록
    # path('closet/detail/top/<int:closet_id>/', views_top.detail_top, name='create'), # 디테일
    # path('closet/delete/top/<int:closet_id>/', views_outer.top_closet_create, name='create'), # 삭제

    # 하의
    path('closet/pants_create/<int:author_user>/', 
    views_pants.closet_create, name='pants_create'), # 등록
    # path('closet/detail/pants/<int:closet_id>/', views_pants.detail_pants, name='create'), # 디테일
    # path('closet/delete/pants/<int:closet_id>/', views_outer.outer_closet_delete, name='create'), # 삭제

    # 아우터
    path('closet/outer_create/<int:author_user>/', 
    views_outer.closet_create, name='outer_create'), # 등록
    # path('closet/detail/outer/<int:closet_id>/', views_outer.detail_outer, name='create'), # 디테일
    # path('closet/delete/outer/<int:closet_id>/', views_outer.outer_closet_delete, name='create'), # 삭제
    
    # 원피스
    path('closet/onepiece_create/<int:author_user>/', 
    views_onepiece.closet_create, name='onepiece_create'), # 등록
    # path('closet/detail/onepiece/<int:closet_id>/', views_onepiece.detail_onepiece, name='create'), # 디테일
    # path('closet/delete/onepiece/<int:closet_id>/', views_outer.outer_closet_delete, name='create'), # 삭제

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)