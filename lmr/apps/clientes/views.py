from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, "clientes/home.html")

# Para procesar a los clientes
def contact_submit(request):
    if request.method == "POST":
        # Aquí procesarías los datos (enviar email, guardar en BD, etc.)
        return HttpResponse("¡Gracias! Hemos recibido tu solicitud.")
    return redirect('informacion')