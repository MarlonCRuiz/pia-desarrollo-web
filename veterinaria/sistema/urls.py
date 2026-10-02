from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('inicio/', views.inicio, name='inicio'),
    path('registrar/', views.registrar, name='registrar'),
    path('consultar/', views.consultar, name='consultar'),
    path('editar/<int:id>/', views.editar, name='editar'),
]