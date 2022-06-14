from django.urls import path
from . import views

urlpatterns = [
    path('',views.api_crud,name='api_crud'),
    path('task-list/',views.taskList,name='tasklist'),
    path('task-details/<str:pk>/',views.taskDetails,name='task-Details'),
    path('task-Create/',views.taskCreate,name='task-create'),
    path('task-update/<str:pk>/',views.taskUpdate,name='task-update'),
    path('task-delete/<str:pk>/',views.taskDelete,name='task-delete'),
    path('hello/',views.Authenti.as_view(),name='authentication')

]