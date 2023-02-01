from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from .models import Brands, Polish
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.urls import reverse


# Create your views here.

class Home(TemplateView):
    template_name='home.html'

class About(TemplateView):
    template_name='about.html'

class BrandList(TemplateView):
    template_name = 'brand_list.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get('name')
        if name != None:
            context['brands'] = Brands.objects.filter(name__icontains=name)
            context["header"] = f'Searching for {name}'
        else:
            context['brands'] = Brands.objects.all()
            context["header"] = 'Polish Brands'
        return context

class BrandPolishes(TemplateView):
    template_name = 'artist_detail.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get('name')
        # WANT TO SEE ALL POLISHES FROM THAT BRAND WHEN A BRAND IS CLICKED ON


class PolishList(TemplateView):
    template_name = 'polish_list.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get('name')
        if name != None:
            context['polishes'] = Polishes.objects.filter(name__icontains=name)
            context["header"] = f'Searching for {name}'
        else:
            context['polishes'] = Polishes.objects.all()
            context["header"] = 'Polishes'
        return context

class PolishCreate(CreateView):
    model = Polish
    fields = ['id', 'name', 'image', 'brand']
    template_name = 'polish_create.html'
    def get_success_url(self):
        return reverse('polish_detail', kwargs={'pk': self.object.pk})

class PolishDetail(DetailView):
    model = Polish
    template_name = 'polish_detail.html'

class PolishUpdate(UpdateView):
    model = Polish
    fields = ['name', 'image', 'brand']
    template_name = 'polish_update.html'
    def get_success_url(self):
        return reverse('polish_detail', kwargs={'pk': self.object.pk})

class PolishDelete(DeleteView):
    model = Polish
    template_name = 'polish_deleted.html'
    success_url = '/polishes/'