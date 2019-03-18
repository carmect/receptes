from django.urls import path
from receptes import views

urlpatterns = [
    path('', views.llista_receptes, name='llista_receptes'),
]