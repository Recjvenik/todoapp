from django.urls import path
from . import views



urlpatterns = [

    path('', views.api_root),
    path('tasks/', views.task_list_view, name='task-list'),
    path('tasks/<int:pk>', views.task_delete, name='task-detail'),
    path('users/', views.user_list_view, name='user-list'),
    path('users/<int:pk>', views.user_detail, name='user-detail'),

    path('cal/', views.TaskList.as_view()),
    path('cal/<int:pk>', views.TaskListDetail.as_view()),
   
]

