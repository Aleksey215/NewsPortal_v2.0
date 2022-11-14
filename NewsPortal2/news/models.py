from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
    """
    Авторы публикаций
    """
    author_user = models.OneToOneField(User, on_delete=models.CASCADE)
    author_rating = models.IntegerField(default=0)

    def update_rating(self):
        """
        Формирование рейтинга автора.
        Он равен сумме рейтингов всех статей умноженному на три плюс сумма рейтингов всех комментариев.
        :return:
        """
        posts = Post.objects.filter(author=self.author_user.id)
        post_rat = 0
        for post in posts:
            post_rat += post.post_rating
        comments = Comment.objects.filter(author=self.author_user.id)
        com_rat = 0
        for comment in comments:
            com_rat += comment.comment_rating
        self.author_rating = post_rat * 3 + com_rat
        self.save()

    def __str__(self):
        return f'{self.author_user}'


class Category(models.Model):
    """
    Категории публикаций
    """
    name = models.CharField(max_length=64, unique=True)
    subscribers = models.ManyToManyField(User)

    def __str__(self):
        return self.name


class Post(models.Model):
    """
    Публикации
    """
    article = 'AR'
    news = 'NW'
    TYPE = (
        (news, 'News'),
        (article, 'Article')
    )
    author = models.ForeignKey(Author, on_delete=models.CASCADE, default=None, blank=True)
    type = models.CharField(max_length=2, choices=TYPE, default=article)
    time_of_creation = models.DateTimeField(auto_now_add=True)
    category = models.ManyToManyField(Category)
    title = models.CharField(max_length=128)
    content = models.TextField()
    post_rating = models.IntegerField(default=0)

    def __str__(self):
        return f'Title:{self.title} In category:{self.category.name}'

    def like(self):
        self.post_rating += 1
        self.save()

    def dislike(self):
        self.post_rating -= 1
        self.save()

    def preview(self):
        return f'{self.content[:125]} + {"..."}'


class Comment(models.Model):
    """
    Комментарии для публикаций
    """
    post = models.ForeignKey(Post, on_delete=models.CASCADE, default=None, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None, blank=True)
    content = models.TextField()
    date_time = models.DateTimeField(auto_now_add=True)
    comment_rating = models.IntegerField(default=0)

    def __str__(self):
        return f'Comment on{self.post} Author: {self.author}'

    def like(self):
        self.comment_rating += 1
        self.save()

    def dislike(self):
        self.comment_rating -= 1
        self.save()
