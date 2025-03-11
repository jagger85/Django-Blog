from django.urls import path    
from . import views

urlpatterns = [
    path('', views.index, name='blog-index'),
    path('posts/', views.posts, name='all-posts'),
    path('posts/<slug:slug>',views.post)
]