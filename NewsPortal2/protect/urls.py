from django.urls import path
from .views import *

urlpatterns = [
    # сама страница профиля
    path('', IndexView.as_view(), name='profile'),
    path('upgrade/', upgrade, name='upgrade'),
    path('downgrade/', downgrade, name='downgrade'),
    ]
