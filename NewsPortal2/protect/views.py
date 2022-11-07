from django.shortcuts import redirect
from django.views.generic import TemplateView
# Ограничение доступа
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group


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
    return redirect('/')
