from django.shortcuts import render
from django.views.generic import CreateView, DetailView, DeleteView, ListView, UpdateView

from .models import Author, Category, Comment, Post
from .filters import PostFilter


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
    ordering = ['-id']
    paginate_by = 10

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())
        return context


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
