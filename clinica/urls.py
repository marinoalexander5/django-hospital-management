from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'clinica'
urlpatterns = [
    path('', views.index, name='index'),
    path('turnos/', views.TurnoListView.as_view(), name='turnos'),    
    path('turnos/create/', views.TurnoCreateView.as_view(), name='turno_create'),
    path('turnos/<int:pk>/update/', views.TurnoUpdateView.as_view(), name='turno_update'),
    path('turnos/<int:pk>/delete/', views.TurnoDeleteView.as_view(), name='turno_delete'),
    path('paciente/create/', views.PacienteCreateView.as_view(), name='paciente_create'),
    path('paciente/<int:pk>/update/', views.PacienteUpdateView.as_view(), name='paciente_update'),
    path('paciente/<int:pk>/delete/', views.PacienteDeleteView.as_view(), name='paciente_delete'),
]