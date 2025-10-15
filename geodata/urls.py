#/*JESUS ESQUIPULAS QUINTINO LEYVA - S22120205*/
from django.urls import path
from . import views

urlpatterns = [
    path('', views.selector_ubicacion, name='selector_ubicacion'), 
    path('ajax/cargar_municipios/', views.cargar_municipios, name='ajax_cargar_municipios'),
]