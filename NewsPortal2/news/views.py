from django.shortcuts import render
from django.views.generic import CreateView, DetailView, DeleteView, ListView

from .models import Author, Category, Comment, Post


class CreatePostView(CreateView):
    """
    Создание публикации
    """
    model = Post


class PostsListView(ListView):
    """
    Список всех публикаций
    """
    pass


class DetailPostView(DetailView):
    """
    Подробная ин-ия о публикации
    """
    pass


class DeletePostView(DeleteView):
    """
    Удаление публикации
    """
    pass
