from django.shortcuts import render
from apps.administracion.models import Administration, StatusEnum, CommunityEnum
from django.shortcuts import render
from django.db.models import Q, Count

# Renderizado de la vista de inicio
def home(request):
    # 1. Las 3 destacadas para el carrusel/mosaico
    destacadas = Administration.objects.filter(featured=True)[:3]

    # 2. El conteo TOTAL de administraciones en la BD
    total_administraciones = Administration.objects.count()

    # 3. Números únicos para filtros 
    numeros_disponibles = Administration.objects.filter(
        status=StatusEnum.AVAILABLE
    ).values_list('number', flat=True).distinct()

    context = {
        'destacadas': destacadas,
        'total_administraciones': total_administraciones, 
        'numeros_disponibles': numeros_disponibles,
    }

    return render(request, "core/home.html", context)

# Mostrar la vista de busqueda
def search(request):
    # 1. Captura de parámetros
    query = request.GET.get('q', '')
    precio_max = request.GET.get('precio', '')
    comunidad_slug = request.GET.get('comunidad', '')
    orden = request.GET.get('orden', '-created_date')

    # 2. BASE PARA LOS CONTADORES (Independiente de la búsqueda por texto)
    # Queremos que los numeritos de los botones NO cambien aunque busques "Valencia"
    base_for_counts = Administration.objects.all()
    
    # Inicializamos el diccionario con todas las comunidades en 0
    full_counts = {code: 0 for code, name in CommunityEnum.choices}
    
    # Contamos sobre la base total (o puedes aplicar solo el filtro de precio si prefieres)
    actual_counts = base_for_counts.values('community').annotate(total=Count('id'))
    for item in actual_counts:
        full_counts[item['community']] = item['total']


    # 3. FILTRADO PARA LOS RESULTADOS (Lo que se ve en las cards)
    results = Administration.objects.all()

    if query:
        results = results.filter(
            Q(name__icontains=query) | 
            Q(city__icontains=query) | 
            Q(province__icontains=query)
        )

    if precio_max:
        try:
            results = results.filter(price__lte=float(precio_max))
        except ValueError: pass

    # Filtro de comunidad (se aplica solo a los resultados finales)
    if comunidad_slug:
        results = results.filter(community=comunidad_slug)

    # 4. Ordenación final
    results = results.order_by(orden)

    context = {
        'results': results,
        'communities': CommunityEnum.choices,
        'counts_dict': full_counts, # Estos números ya no cambiarán al buscar texto
        'query': query,
        'comunidad_seleccionada': comunidad_slug,
        'precio_seleccionado': precio_max,
        'orden_seleccionado': orden,
    }
    return render(request, 'core/search.html', context)

from django.http import JsonResponse

# Autocompletado de la barra de busqueda
def autocomplete(request):
    term = request.GET.get('term', '')
    # Buscamos por nombre, ciudad o provincia para que sea más útil
    results = Administration.objects.filter(
        Q(name__icontains=term) | 
        Q(city__icontains=term) | 
        Q(province__icontains=term)
    ).values_list('name', flat=True).distinct()[:8]
    
    return JsonResponse(list(results), safe=False)