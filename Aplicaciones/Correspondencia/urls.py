from django.urls import path
from .import views

urlpatterns = [
    path('', views.home),
    path('registroRecibido/', views.registroRecibido),
    path('edicionRecibido/<codigo>', views.edicionRecibido), 
    path('editarRecibido/', views.editarRecibido),
]