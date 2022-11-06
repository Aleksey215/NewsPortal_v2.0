from django.urls import path
from .views import IndexView

urlpatterns = [
    # сама страница профиля
    path('', IndexView.as_view(), name='profile'),
    ]
