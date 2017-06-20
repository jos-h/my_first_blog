from django.shortcuts import render
from .models import Post
from django.contrib.auth.models import User

# Create your views here.


def post_list(request):
    author_name = User.objects.get(username='kunal')
    posts_author_name = Post.objects.filter(author= author_name)#.order_by('published_date')
    text_data = Post.objects.values().order_by('text')
    return render(request, 'Blog/post_list.html', {'posts_author_name': posts_author_name,'text_data': text_data})
