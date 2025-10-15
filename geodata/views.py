# JESUS ESQUIPULAS QUINTINO LEYVA
import json
from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings
import os

DATA_PATH = os.path.join(settings.BASE_DIR, 'geodata', 'estados-municipios.json')

def load_data():
    """Carga los datos desde el archivo JSON."""
    try:
        with open(DATA_PATH, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo de datos en {DATA_PATH}")
        return []

def selector_ubicacion(request):
    """Vista 1: Renderiza el formulario con la lista inicial de estados."""
    data = load_data()
    estados = [{'id': estado['id'], 'nombre': estado['nombre']} for estado in data]
    
    return render(request, 'geodata/select_ubicacion.html', {'estados': estados})

def cargar_municipios(request):
    """Vista 2: La función AJAX. Recibe estado_id y retorna municipios en JSON."""
    
    estado_id = request.GET.get('estado_id')
    municipios_list = []

    if estado_id:
        data = load_data()
        try:
            estado_id = int(estado_id) 
            
            estado_seleccionado = next(
                (e for e in data if e['id'] == estado_id), None
            )
            
            if estado_seleccionado:
                municipios_list = estado_seleccionado.get('municipios', [])
            
        except ValueError:
            pass 
    return JsonResponse({'municipios': municipios_list})