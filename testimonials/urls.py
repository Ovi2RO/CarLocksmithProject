from django.urls import path
from .views import TestimonialsListView, TestimonialsCreateView

urlpatterns = [
    path('list', TestimonialsListView.as_view(), name='testimonials-list'),
    path('', TestimonialsCreateView.as_view(), name='testimonials'),
]