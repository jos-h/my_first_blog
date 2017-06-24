from django.shortcuts import render
from .models import Post
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404,redirect
from .forms import PostForm
from django.utils import timezone

# Create your views here.


def post_list(request):
    author_name = User.objects.get(username='kunal')
    posts_author_name = Post.objects.filter(author= author_name)#.order_by('published_date')
    text_data = Post.objects.values().order_by('text')
    return render(request, 'Blog/post_list.html', {'posts_author_name': posts_author_name})


def post_detail(request, pk):

    post = get_object_or_404(Post, pk=pk)
    return render(request, 'Blog/post_detail.html', {'post': post})


def post_new(request):

    if request.method == 'GET':
        form = PostForm(request.GET)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
        else:
            form = PostForm()
    return render(request, 'Blog/post_edit.html', {'post_form': form})


def post_edit(request, pk):

    post = get_object_or_404(Post, pk=pk)
    if request.method == 'GET':
        form = PostForm(request.GET, instance=post)

        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
        else:
            form = PostForm(instance=post)
    return render(request, 'Blog/post_edit.html', {'post_form': form})



