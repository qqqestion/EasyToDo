from django.urls import path

from . import views


urlpatterns = [
    path('home/', views.home, name='home'),
    path('complete_task/<int:pk>/', views.complete_task, name='complete-task'),
]

