from django.contrib.auth.models import User
from django.urls.base import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView


class UserList(ListView):
    model = User


class UserCreate(CreateView):
    model = User
    fields = ['username', 'first_name', 'last_name', 'email', 'is_staff']
    success_url = reverse_lazy('user-list')
