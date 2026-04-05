from django.shortcuts import render, redirect
from django.contrib import messages
from .models import ClienteContacto

# Create your views here.
def home(request):
    return render(request, "clientes/home.html")

# Añadir cliente a la base de datos
def contact_submit(request):
    if request.method == "POST":
        # 1. Extraemos los datos
        nombre = request.POST.get('nombre')
        email = request.POST.get('email')
        telefono = request.POST.get('telefono')
        interes = request.POST.get('interes')
        mensaje = request.POST.get('mensaje')

        try:
            # 2. Guardamos en BD
            ClienteContacto.objects.create(
                nombre=nombre,
                email=email,
                telefono=telefono,
                interes=interes,
                mensaje=mensaje
            )
            messages.success(request, "¡Gracias! Tu solicitud ha sido enviada correctamente.")
            
        except Exception:
            messages.error(request, "Hubo un error al procesar tu solicitud.")

        # 3. REDIRECCIÓN DINÁMICA:
        # request.META.get('HTTP_REFERER') obtiene la URL exacta de donde venía el usuario.
        # Si por algún motivo no existe (raro), lo mandamos a 'home' como respaldo.
        return redirect(request.META.get('HTTP_REFERER', 'home'))
    
    return redirect('home')