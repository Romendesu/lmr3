from django.shortcuts import render, get_object_or_404
from .models import Administration

def administration_detail(request, pk):
    # pk ahora será el UUID que viene de la URL
    administration = get_object_or_404(Administration, pk=pk)
    return render(request, 'administracion/home.html', {'admin': administration})