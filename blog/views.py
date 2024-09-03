from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse

from .forms import PostForm
from .models import Post


"""
FBV - Function based views (Предстовления основоных на функциях)
CBV - Class based views (Предстовление основаных на классах)
"""

def root(request):
    return render(request, template_name='blog/index.html')


def index(request):
    return render(request, template_name='blog/index.html')


def about(request):
    context = {
        'name': 'Дмитрий',
        'lastname': 'Горим',
        'email': 'd.gorin@mail.ru',
        'title': 'О сайте'
    }
    return render(request, template_name='blog/about.html', context=context)

def add_post(request):
    if request.method == "GET":
        form = PostForm()
        context = {
            'form': form,
            'title': 'Добовления поста'
        }
        return render(request, template_name='blog/add_post.html', context=context)

    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

        return index(request)


def post_list(request):
    # Получаем все объект модели Post
    posts = Post.objects.all()
    context = {
        'title': 'Посты',
        'posts': posts
    }
    return render(request, template_name='blog/posts.html', context=context)


def post_detail(request, pk):
    # Получаем объект с задоным pk(ключем)
    post = get_object_or_404(Post, pk=pk)
    context = {
        'title': 'Информация о посте',
        'post': post
    }
    return render(request, template_name='blog/post_detail.html', context=context)


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(data=request.POST, instance=post)
        if form.is_valid():
            form.save()
            return post_list(request)

    else:
        form = PostForm(instance=post)

    context = {
        'forma': form,
        'title': 'Редактировать пост'
    }
    return render(request, template_name='blog/post_edit.html', context=context)


def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)