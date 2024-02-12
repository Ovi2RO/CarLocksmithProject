from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from .models import Testimony

class TestimonialsListView(ListView):
    model = Testimony
    template_name = 'testimony/testimonies.html'
    context_object_name = 'testimonies'

class TestimonialsCreateView(CreateView):
    model = Testimony
    fields = ['name', 'content']
    template_name = 'testimony/testimonies.html'
    success_url = reverse_lazy("testimonials")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        testimonies = Testimony.objects.all()
        context['testimonies'] = testimonies
        return context
    


