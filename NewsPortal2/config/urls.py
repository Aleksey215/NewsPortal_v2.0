from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # для подключения адресов приложения "news"
    path('', include('news.urls')),
    # для подключения адресов "allauth"
    path('accounts/', include('allauth.urls')),
    # для личного кабинета пользователя
    path('protect/', include('protect.urls')),
]
