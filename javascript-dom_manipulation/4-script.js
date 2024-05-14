const evento = document.getElementById('add_item');
const elemento = document.querySelector('.my_list');

evento.addEventListener('click', function() {
    const nuevo = document.createElement('li');
    nuevo.innerText = 'Item';
    elemento.appendChild(nuevo);
});