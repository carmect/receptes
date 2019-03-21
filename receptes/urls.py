from django.urls import path
from receptes import views

urlpatterns = [
    path('', views.llista_receptes, name='llista_receptes'),
    path('recepta/<int:pk>/', views.recepta_detall, name='recepta_detall'),
    path('recepta/new', views.recepta_new, name='recepta_new'),
]