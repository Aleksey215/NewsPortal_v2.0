from django.db import models
from allauth.account.forms import SignupForm
from django.contrib.auth.models import Group


# to automatically add a user to a group upon registration
class BasicSignupForm(SignupForm):

    def save(self, request):
        user = super(BasicSignupForm, self).save(request)
        common_group = Group.objects.get(name='Common')
        common_group.user_set.add(user)
        return user
