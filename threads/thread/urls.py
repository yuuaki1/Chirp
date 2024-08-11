from django.urls import path 
from . import views

urlpatterns = [
   path('', views.thread_list, name='thread_list'),
   path('create/', views.thread_create, name='thread_create'),
   path('<int:thread_id>/edit/', views.thread_edit, name='thread_edit'),
   path('<int:thread_id>/delete/', views.thread_delete, name='thread_delete'),
   path('register/', views.register, name='register'),
] 


