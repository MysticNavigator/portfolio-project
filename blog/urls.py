
from django.urls import path

from . import views


urlpatterns = [
    path('', views.allblogs, name='allblogs'),
    path('<int:blog_id>/', views.detail, name='detail'),
    path('bio', views.allblogs, name='bio'),
    path('video', views.allblogs, name='video')
] 