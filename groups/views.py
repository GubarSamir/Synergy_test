from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from .models import Group
from .forms import GroupCreateForm, GroupUpdateForm

from users.models import User


class GroupListView(LoginRequiredMixin, ListView):
    paginate_by = 5
    model = Group
    template_name = 'groups/list.html'


class GroupCreateView(SuccessMessageMixin, CreateView):
    model = Group
    form_class = GroupCreateForm
    success_url = reverse_lazy('groups:list')
    success_message = 'Group create'
    template_name = 'groups/create.html'


class GroupDeleteView(DeleteView):
    model = Group
    success_url = reverse_lazy('groups:list')
    template_name = 'groups/test_delet.html'


class GroupUpdateView(UpdateView):
    model = Group
    form_class = GroupUpdateForm
    success_url = reverse_lazy('groups:list')
    template_name = 'groups/update.html'

    pk_url_kwarg = 'ppk'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['users'] = self.get_object().users.select_related('group', 'headed_group').all()

        return context

    def get_initial(self):
        initial = super().get_initial()
        try:
            initial['headman_field'] = self.object.headman.id
        except AttributeError as ex:
            pass

        return initial

    def form_valid(self, form):
        respose = super().form_valid(form)
        form.instance.headman = User.objects.get(id=form.cleaned_data['headman_field'])
        form.instance.save()

        return respose