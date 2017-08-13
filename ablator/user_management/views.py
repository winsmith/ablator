from django.contrib.auth.models import User
from django.views.generic.list import ListView


class UserList(ListView):
    model = User
