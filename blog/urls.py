from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.create_post, name='add'),
    path('view/<int:pk>/', views.view_post, name='view'),
    path('edit/<int:pk>/', views.edit_post, name='edit'),
    path('delete/<int:pk>/', views.delete_post, name='delete'),
]
