from django.contrib.auth.models import User
from django.urls.base import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.contrib.admin.views.decorators import staff_member_required


@method_decorator(staff_member_required, name='dispatch')
class UserList(ListView):
    model = User


@method_decorator(staff_member_required, name='dispatch')
class UserCreate(CreateView):
    model = User
    fields = ['username', 'first_name', 'last_name', 'email', 'is_staff']
    success_url = reverse_lazy('user-list')


@method_decorator(staff_member_required, name='dispatch')
class UserUpdate(UpdateView):
    model = User
    fields = ['username', 'first_name', 'last_name', 'email', 'is_staff']
    success_url = reverse_lazy('user-list')


@method_decorator(staff_member_required, name='dispatch')
class UserDelete(DeleteView):
    model = User
    success_url = reverse_lazy('user-list')
