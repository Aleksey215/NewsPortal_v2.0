from django.shortcuts import redirect
from django.views.generic import TemplateView
# Ограничение доступа
from django.contrib.auth.mixins import LoginRequiredMixin


class IndexView(LoginRequiredMixin, TemplateView):
    """
    Ограничение доступа к странице с профилем (только для зарегистрированных).
    """
    template_name = 'profile.html'
