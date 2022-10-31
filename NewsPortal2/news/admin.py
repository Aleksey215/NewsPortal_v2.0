from django.contrib import admin
from django import forms

from .models import Author, Category, Comment, Post


class AuthorAdminForm(forms.ModelForm):

    class Meta:
        model = Author
        fields = '__all__'


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    form = AuthorAdminForm
    list_display = ['author_user', 'author_rating', 'id']
    list_display_links = ['author_user']


class CategoryAdminForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = '__all__'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    form = CategoryAdminForm
    list_display = ['name', 'id']
    list_display_links = ['name']


class CommentAdminForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = '__all__'


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    form = CommentAdminForm
    list_display = ['post', 'author', 'content', 'date_time']
    list_display_links = ['post']


class PostAdminForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = '__all__'


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm
    list_display = [
        'title',
        'author',
        'type',
        'categories',
        'time_of_creation'
    ]
    list_display_links = ['title']

    def categories(self, obj):
        return ",\n".join([str(c) for c in obj.category.all()])
