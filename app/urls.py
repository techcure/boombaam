from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path, re_path
from app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Matches any html file 
    re_path(r'^.*\.html', views.pages, name='pages'),
    # The home page
    path('', views.index, name='home'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/new1/', views.post_new, name='post_new1'),
]+ static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
