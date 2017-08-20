from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.urls.base import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.contrib.admin.views.decorators import staff_member_required

from user_management.models import AblatorUser, Organization


@method_decorator(staff_member_required, name='dispatch')
class UserList(ListView):
    model = User

    def get_queryset(self):
        return User.objects.filter(ablatoruser__organization=self.request.user.ablatoruser.organization)


@method_decorator(staff_member_required, name='dispatch')
class UserCreate(CreateView):
    model = User
    fields = ['username', 'first_name', 'last_name', 'email', 'is_staff']
    success_url = reverse_lazy('user-list')

    def form_valid(self, form):
        form.instance.save()
        ablatoruser = AblatorUser(user=form.instance, organization=self.request.user.ablatoruser.organization)
        ablatoruser.save()
        form.instance.ablatoruser = ablatoruser
        return super().form_valid(form)


@method_decorator(staff_member_required, name='dispatch')
class UserUpdate(UpdateView):
    model = User
    fields = ['username', 'first_name', 'last_name', 'email', 'is_staff']
    success_url = reverse_lazy('user-list')

    def get_queryset(self):
        return User.objects.filter(ablatoruser__organization=self.request.user.ablatoruser.organization)


@method_decorator(staff_member_required, name='dispatch')
class UserDelete(DeleteView):
    model = User
    success_url = reverse_lazy('user-list')

    def get_queryset(self):
        return User.objects.filter(ablatoruser__organization=self.request.user.ablatoruser.organization)


@method_decorator(staff_member_required, name='dispatch')
class OrganizationUpdate(UpdateView):
    model = Organization
    success_url = reverse_lazy('user-list')
    fields = ['name', 'slug']

    def get_queryset(self):
        return Organization.objects.filter(id=self.request.user.ablatoruser.organization.id)


@method_decorator(login_required, name='dispatch')
class UserDetail(DetailView):
    model = User

    def get_queryset(self):
        return User.objects.filter(id=self.request.user.id)