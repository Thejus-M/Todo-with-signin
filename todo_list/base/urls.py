from django.contrib.auth.views import LogoutView
from django.urls import path

from .views import (CustomLoginView, RegisterPage, TaskCreateView,
                    TaskDeleteView, TaskDetail, TaskList, TaskUpdateView)

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', RegisterPage.as_view(), name='register'),
    
    path('',TaskList.as_view(),name='tasks'),
    path('task/<int:pk>/',TaskDetail.as_view(),name='task'),
    path('create-task/',TaskCreateView.as_view(),name='create-task'),
    path('update-task/<int:pk>/',TaskUpdateView.as_view(),name='update-task'),
    path('delete-task/<int:pk>/',TaskDeleteView.as_view(),name='delete-task'),
]
