from django.urls import path

from .views import TaskCreateView,TaskDeleteView ,TaskDetail, TaskList, TaskUpdateView

urlpatterns = [
    path('',TaskList.as_view(),name='tasks'),
    path('task/<int:pk>/',TaskDetail.as_view(),name='task'),
    path('create-task/',TaskCreateView.as_view(),name='create-task'),
    path('update-task/<int:pk>/',TaskUpdateView.as_view(),name='update-task'),
    path('delete-task/<int:pk>/',TaskDeleteView.as_view(),name='delete-task'),
]
