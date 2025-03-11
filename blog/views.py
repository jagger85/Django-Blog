from django.shortcuts import render

def index(request):
    return render(request, 'blog/index.html')

def posts(request):
    return render(request, 'blog/posts.html')

def post(request, slug):
    return render(request, 'blog/post.html',{'postname':slug})