from django.urls import path
from .views import views_outer, views_pants, views_top, views_onepiece, views_base
from django.conf.urls.static import static
from django.conf import settings

app_name = 'closet'

urlpatterns = [
    
    # path('', views_base.index, name='index'),
    path('<int:author_user>/<int:closet_id>/', 
    views_base.detail, name ='detail'),
    
    # 상의
    path('closet/closet_top/<int:author_user>/', 
    views_top.top_closet_create, name='top_create'), # 등록
    # path('closet/detail/top', views_outer.top_closet_detail, name='create'), # 디테일
    # path('closet/delete/top', views_outer.top_closet_create, name='create'), # 삭제
    # 하의
    path('closet/closet_pants/<int:author_user>/', 
    views_pants.pants_closet_create, name='pants_create'), # 등록
    # path('closet/detail/pants', views_outer.outer_closet_detail, name='create'), # 디테일
    # path('closet/delete/pants', views_outer.outer_closet_delete, name='create'), # 삭제
    # 아우터
    path('closet/closet_outer/<int:author_user>/', 
    views_outer.outer_closet_create, name='outer_create'), # 등록
    # path('closet/detail/outer', views_outer.outer_closet_detail, name='create'), # 디테일
    # path('closet/delete/outer', views_outer.outer_closet_delete, name='create'), # 삭제
    # 원피스
    path('closet/closet_onepiece/<int:author_user>/', 
    views_onepiece.onepiece_closet_create, name='onepiece_create'), # 등록
    # path('closet/detail/onepiece', views_outer.outer_closet_detail, name='create'), # 디테일
    # path('closet/delete/onepiece', views_outer.outer_closet_delete, name='create'), # 삭제

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)