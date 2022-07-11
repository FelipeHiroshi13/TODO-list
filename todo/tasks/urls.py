from django.urls import path, include

from . import views

urlpatterns = [
    path('helloword/', views.helloWord),
    path('', views.taskList, name='task-list'),
    path('yourname/<str:name>', views.yourName, name='your-name')
]
