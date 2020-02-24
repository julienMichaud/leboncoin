from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from .models import Annonce
from .filters import AnnonceFilter

class AnnonceCreateView(LoginRequiredMixin,CreateView):
    model = Annonce
    template_name = 'annonce_new.html'
    fields = ('title', 'category', 'price', 'description', 'photo')
    login_url = 'login'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class AnnonceListView(LoginRequiredMixin,ListView):
    model = Annonce
    template_name = 'annonce_list.html'
    login_url = 'login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = AnnonceFilter(self.request.GET, queryset=self.get_queryset())
        return context

class OwnAnnonceListView(LoginRequiredMixin,ListView):
    model = Annonce
    template_name = 'annonce_own_list.html'
    login_url = 'login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = AnnonceFilter(self.request.GET, queryset=self.get_queryset())
        return context
    
    def get_queryset(self):
        return self.model.objects.filter(author=self.request.user)

    




class AnnonceUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Annonce
    fields = ('title', 'category', 'price', 'description', 'photo')
    template_name = 'annonce_edit.html'
    login_url = 'login'

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class AnnonceDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Annonce
    template_name = 'annonce_delete.html'
    success_url = reverse_lazy('Annonce_list')
    login_url = 'login'

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user