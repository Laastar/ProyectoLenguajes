from django.urls import path
from . import views

urlpatterns = [
	path('', views.inicio, name='inicio'),
	path('objetivo/', views.objetivo, name='objetivo'),
	path('datos/', views.datos, name='datos'),
	path('cuestionario/', views.cuestionario, name='cuestionario'),
	path('terminar/', views.terminar, name='terminar')
]