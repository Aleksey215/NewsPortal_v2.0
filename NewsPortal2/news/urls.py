from django.urls import path

from .views import *


urlpatterns = [
    path('', ListPostsView.as_view(), name='posts_list'),
    path('post_create/', CreatePostView.as_view(), name='post_create'),
    path('post_detail/<int:pk>', DetailPostView.as_view(), name='post_detail'),
    path('post_delete/<int:pk>', DeletePostView.as_view(), name='post_delete'),
]
