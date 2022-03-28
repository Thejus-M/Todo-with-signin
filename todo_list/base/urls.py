from django.urls import path
from .views import TaskList,TaskDetail,TaskCreateView

urlpatterns = [
    path('',TaskList.as_view(),name='tasks'),
    path('task/<int:pk>/',TaskDetail.as_view(),name='task'),
    path('create-task/',TaskCreateView.as_view(),name='create-task'),
]