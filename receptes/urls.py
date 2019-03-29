from django.urls import path
from receptes import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.llista_receptes, name='llista_receptes'),
    path('recepta/<int:pk>/', views.recepta_detall, name='recepta_detall'),
    path('recepta/new', views.recepta_new, name='recepta_new'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)