from django.urls import path
from .views import GalleryCreateView, GalleryView

urlpatterns = [
    path('', GalleryCreateView.as_view(), name='gallery'),
    path('list', GalleryView.as_view(), name='gallery-list'),
]