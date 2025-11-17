from django.urls import path    
from . import views

app_name = 'blog'

urlpatterns = [
    path('posts/', views.posts, name='all-posts'),
    path('posts/<slug:slug>',views.post_detail, name='post-detail-page')
]