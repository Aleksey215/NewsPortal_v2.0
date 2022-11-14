from django.shortcuts import redirect
from django.views.generic import TemplateView
# Ограничение доступа
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

from news.models import Author


class IndexView(LoginRequiredMixin, TemplateView):
    """
    Ограничение доступа к странице с профилем (только для зарегистрированных).
    """
    template_name = 'profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context['is_not_author'] = not user.groups.filter(name='authors').exists()
        return context


@login_required
def upgrade(request):
    user = request.user
    authors_group = Group.objects.get(name='authors')
    if not user.groups.filter(name='authors').exists():
        authors_group.user_set.add(user)
        Author.objects.create(author_user=user)
    return redirect('/')


@login_required
def downgrade(request):
    user = request.user
    authors_group = Group.objects.get(name='authors')
    if user.groups.filter(name='authors').exists():
        authors_group.user_set.remove(user)
        Author.objects.get(author_user=user).delete()
    return redirect('/')
