const elemento = document.getElementById('red_header');
const etiqueta = document.querySelector('header');

elemento.addEventListener('click', function() {
    etiqueta.style.color = '#ff0000'
})