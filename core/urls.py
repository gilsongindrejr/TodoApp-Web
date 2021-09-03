from django.urls import path

from .views import IndexView, CreateView, UpdateView, DeleteView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('create/', CreateView.as_view(), name='create'),
    path('update/', UpdateView.as_view(), name='update'),
    path('delete/', DeleteView.as_view(), name='delete'),
]
