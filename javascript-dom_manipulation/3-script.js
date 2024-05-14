const etiqueta = document.getElementById('toggle_header');
const elemento = document.querySelector('header');

etiqueta.addEventListener('click', function() {
    if (elemento.classList.contains('green')){
        elemento.classList.remove('green');
        elemento.classList.add('red');
    }
    else {
        elemento.classList.remove('red');
        elemento.classList.add('green');
    }
});