from django.urls import path

from .views import IndexView, CreateTaskView, UpdateTaskView, DeleteTaskView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('create/', CreateTaskView.as_view(), name='create'),
    path('<int:pk>/update/', UpdateTaskView.as_view(), name='update'),
    path('<int:pk>/delete/', DeleteTaskView.as_view(), name='delete'),
]
