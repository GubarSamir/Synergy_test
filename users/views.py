from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse, reverse_lazy
from django.shortcuts import render, get_object_or_404  # noqa
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from django.contrib import messages

from core.views import EditView
from users.forms import UserCreateForm, UserUpdateForm, usersFilter
from users.models import User

from webargs.djangoparser import use_kwargs, use_args
from webargs import fields
from copy import copy


def hello(request):
    return HttpResponse('Hello')


class UserCreateView(SuccessMessageMixin, CreateView):
    model = User
    form_class = UserCreateForm
    success_url = reverse_lazy('users:list')
    success_message = 'User has create'
    template_name = 'users/create.html'


class UserListView(LoginRequiredMixin, ListView):
    paginate_by = 10

    model = User
    template_name = 'users/list.html'

    def get_filter(self):
        return usersFilter(
            data=self.request.GET,
            queryset=self.model.objects.all().select_related('group', 'headed_group')
        )

    def get_queryset(self):
        return self.get_filter().qs

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_filter'] = self.get_filter()

        params = self.request.GET
        if 'page' in params:
            params = copy(params)
            del params['page']

        context['get_params'] = params.urlencode()

        return context


class UpdateUserView(EditView):
    model = User
    form_class = UserUpdateForm
    success_url = 'users:list'
    template_name = 'users/update.html'


class UserUpdateView(UpdateView):
    model = User
    form_class = UserUpdateForm
    success_url = reverse_lazy('users:list')
    template_name = 'users/update.html'


class UserDeleteView(DeleteView):
    model = User
    success_url = reverse_lazy('users:list')
    template_name = 'users/delete.html'