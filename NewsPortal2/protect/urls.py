from django.urls import path
from .views import IndexView, upgrade

urlpatterns = [
    # сама страница профиля
    path('', IndexView.as_view(), name='profile'),
    path('upgrade/', upgrade, name='upgrade'),
    ]
