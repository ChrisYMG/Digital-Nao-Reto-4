document.addEventListener('DOMContentLoaded', cargarContenido);
window.addEventListener('scroll', () => {
    if (window.innerHeight + window.scrollY >= document.body.offsetHeight) {
        cargarContenido();
    }
});

function cargarContenido() {
    for (let i = 0; i < 20; i++) {
        const elemento = document.createElement('div');
        elemento.textContent = `Elemento ${document.getElementById('contenido').children.length + 1}`;
        document.getElementById('contenido').appendChild(elemento);
    }
}