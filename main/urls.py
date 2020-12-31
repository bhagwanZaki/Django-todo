from django.urls import path,include
from .views import *
urlpatterns = [
    path('', index, name='index'),
    path('todo/', listTodo.as_view(), name='todo-list'),
    path('create/', createTodo.as_view(), name='create-todo'),
    path('<int:pk>/', detailTodo.as_view(), name='detail-todo'),
    path('update/<int:pk>/', updateTodo.as_view(), name='update-todo'),
    path('completed/<int:pk>/', completed, name='completed')
]   