from django.shortcuts import render
from django.views.generic import CreateView, DetailView, DeleteView, ListView, UpdateView

from .models import Author, Category, Comment, Post


class CreatePostView(CreateView):
    """
    Создание публикации
    """
    model = Post
    template_name = 'post_create.html'
    fields = ('author', 'type', 'title', 'content', 'category')
    success_url = '/'


class ListPostsView(ListView):
    """
    Список всех публикаций
    """
    model = Post
    template_name = 'post_list.html'
    context_object_name = 'posts'


class DetailPostView(DetailView):
    """
    Подробная ин-ия о публикации
    """
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post'


class UpdatePostView(UpdateView):
    model = Post
    template_name = 'post_create.html'
    fields = ('author', 'type', 'title', 'content', 'category')
    success_url = '/'


class DeletePostView(DeleteView):
    """
    Удаление публикации
    """
    model = Post
    template_name = 'post_delete.html'
    success_url = '/'
