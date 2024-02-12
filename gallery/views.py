from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from .models import Picture


class GalleryView(ListView):
    model = Picture
    template_name = 'gallery/gallery.html'
    context_object_name = 'pictures'


class GalleryCreateView(CreateView):
    model = Picture
    fields = ['image', 'content']
    template_name = 'gallery/gallery.html'
    success_url = reverse_lazy("gallery")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pictures = Picture.objects.all()
        context['pictures'] = pictures
        return context
    
    
