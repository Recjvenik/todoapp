from django.urls import path
from . import views

urlpatterns = [

    path('', views.todoList, name='todos'),
    path('todo-create/', views.todoCreate, name='todo-create'),
    path('todo-update/<int:pk>/', views.todoUpdate, name='todo-update'),
    path('todo-delete/<int:pk>/', views.todoDelete, name='todo-delete'),
    path('register/', views.registerUser, name='register'),
    path('login/', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),

]