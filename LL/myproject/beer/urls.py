from django.urls import path
from . import views

urlpatterns = [
    path('', views.index ,name = 'index'),
    path('ver1', views.ver1, name = 'ver1'),
    # 회원가입
    #path('register/',views.register),
    #path('ver2', views.ver2, name = 'ver2'),
]