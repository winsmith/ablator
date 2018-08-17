from django.contrib.auth.decorators import login_required
from django.urls.base import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from core.models import RolloutStrategy, Functionality


@method_decorator(login_required, name='dispatch')
class RolloutStrategyCreate(CreateView):
    model = RolloutStrategy
    fields = ['priority', 'start_at', 'possible_flavors', 'max_enabled_users', 'tag', 'strategy']

    def form_valid(self, form):
        functionality_id = self.kwargs.get('pk')
        functionality = Functionality.objects.get(id=functionality_id)
        form.instance.functionality = functionality
        return super(RolloutStrategyCreate, self).form_valid(form)


@method_decorator(login_required, name='dispatch')
class RolloutStrategyUpdate(UpdateView):
    model = RolloutStrategy
    fields = ['priority', 'start_at', 'possible_flavors', 'max_enabled_users', 'tag', 'strategy']


@method_decorator(login_required, name='dispatch')
class RolloutStrategyDelete(DeleteView):
    model = RolloutStrategy
    success_url = reverse_lazy('home')
