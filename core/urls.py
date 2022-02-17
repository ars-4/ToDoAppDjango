from django.urls import path
from core import views

urlpatterns = [
    path('', views.getRoutes),
    path('notes/', views.getNotes),
    path('notes/<str:pk>/', views.getNote),
    path('note/create/', views.createNote),
    path('notes/<str:pk>/update/', views.updateNote),
    path('notes/<str:pk>/delete/', views.deleteNote),
]