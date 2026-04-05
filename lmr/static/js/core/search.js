// Mejora de la barra de busqueda
document.addEventListener('DOMContentLoaded', function() {
    const input = document.getElementById('search-input');
    const box = document.getElementById('suggestions-box');

    input.addEventListener('input', function() {
        const query = this.value.trim();

        if (query.length < 2) {
            box.classList.add('d-none');
            return;
        }

        fetch(`/autocomplete/?term=${encodeURIComponent(query)}`)
            .then(response => response.json())
            .then(data => {
                if (data.length > 0) {
                    box.innerHTML = '';
                    data.forEach(item => {
                        // Creamos cada elemento de la lista 
                        const button = document.createElement('button');
                        button.type = 'button';
                        button.className = 'list-group-item list-group-item-action border-0 py-3';
                        button.innerHTML = `<i class="bi bi-search me-3 text-muted"></i>${item}`;
                        
                        // Al hacer clic, se rellena el input y se envía el formulario
                        button.onclick = () => {
                            input.value = item;
                            input.form.submit();
                        };
                        box.appendChild(button);
                    });
                    box.classList.remove('d-none');
                } else {
                    box.classList.add('d-none');
                }
            });
    });

    // Cerrar el despliegue si el usuario hace clic fuera
    document.addEventListener('click', function(e) {
        if (!input.contains(e.target) && !box.contains(e.target)) {
            box.classList.add('d-none');
        }
    });
});