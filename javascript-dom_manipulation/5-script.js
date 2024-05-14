const elemento = document.getElementById('update_header');
const update = document.querySelector('header');

elemento.addEventListener('click', function() {
    update.innerText = 'New Header!!!';
});