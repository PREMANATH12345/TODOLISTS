# from typing import Any
from django.shortcuts import render,redirect
from .models import info
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth  import login


class list(LoginRequiredMixin,ListView):
    model = info
    context_object_name='list'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['list'] = context['list'].filter(user=self.request.user)
        context['count'] = context['list'].filter(complete=False).count()
        return context


class detail(LoginRequiredMixin,DetailView):
    model = info
    template_name='APP/detial.html'

class create(LoginRequiredMixin,CreateView):
    model=info
    # fields="__all__"
    fields=['title','des','complete']
    success_url=reverse_lazy('list')
    def form_valid(self,form):
        form.instance.user = self.request.user
        return super(create,self).form_valid(form) 
       
class update(LoginRequiredMixin,UpdateView):
    model=info
    fields=['title','des','complete']
    success_url=reverse_lazy('list')

class delete(LoginRequiredMixin,DeleteView):
    model=info
    context_object_name='list'
    success_url=reverse_lazy('list')

class login(LoginView):
    template_name = 'APP/login.html'
    fields ="__all__"
    redirect_authenticated_user =False

    def get_success_url(self) :
        return reverse_lazy('list')


class register(FormView):
    template_name='APP/sign.html'
    form_class = UserCreationForm
    redirect_authenticated_user=True
    success_url=reverse_lazy('list')

    def form_valid(self,form):
        user = form.save()
        if user is not None:
            login(self.request.user)
        return super(register,self).form_valid(form)
    def get(self,*args,**kwargs):
        if self.request.user.is_authenticated:
            return redirect('list')
        return super(register,self).get(*args,*kwargs)
