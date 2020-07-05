from django.shortcuts import render

from .models import (Rubric, Post, Comments,)


def index(request):
    context = {}
    rubric_qs = Rubric.objects.all()
    context['rubrics'] = rubric_qs
    return render(request, 'index.html', context)


def rubrics_list(request):
    rubric_qs = Rubric.objects.all()
    context = {'rubrics': rubric_qs,
               }
    return render(request, 'rubriclist.html', context)


def post_of_rubric(request):
    context = {}
    pass


def posts_list(request):
    posts_qs = Post.objects.order_by('-updated_at')
    context = {'posts_list': posts_qs,
               }
    return render(request, 'posts.html', context)
