from django.shortcuts import render, redirect
from django.views.generic import CreateView, DetailView, DeleteView, ListView, UpdateView

from .models import Author, Category, Comment, Post
from .filters import PostFilter
from .forms import CommentForm


class PostCreateView(CreateView):
    """
    Создание публикации
    """
    model = Post
    template_name = 'post_create.html'
    fields = ('author', 'type', 'title', 'content', 'category')
    success_url = '/'


class PostsListView(ListView):
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


class PostDetailView(DetailView):
    """
    Подробная ин-ия о публикации
    """
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # добавление формы комментариев
        context['comment_form'] = CommentForm()
        return context

    def post(self, request, pk):
        """
        для добавления формы отклика на страницу объявления
        пользователь может оставить отклик на странице post_detail
        :param request:
        :param pk:
        :return:
        """
        post = self.get_object(pk=pk)
        form = CommentForm(request.POST)

        if form.is_valid():
            obj = form.save(commit=False)
            obj.post = post
            obj.author = self.request.user
            obj.save()
            return redirect('post_detail', post.pk)


class PostUpdateView(UpdateView):
    """
    Редактирование публикации
    """
    model = Post
    template_name = 'post_create.html'
    fields = ('author', 'type', 'title', 'content', 'category')
    success_url = '/'


class PostDeleteView(DeleteView):
    """
    Удаление публикации
    """
    model = Post
    template_name = 'post_delete.html'
    success_url = '/'
