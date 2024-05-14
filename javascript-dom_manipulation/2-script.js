const etiqueta = document.getElementById('red_header');
const elemento = document.querySelector('header');

etiqueta.addEventListener('click', function() {
    elemento.classList.add('red');
});