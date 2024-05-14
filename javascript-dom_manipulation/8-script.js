document.addEventListener('DOMContentLoaded', function() {
    
    fetch('https://hellosalut.stefanbohacek.dev/?lang=fr')
        .then(Response => Response.json())
        .then(data => {
            const elemento = document.getElementById('hello');
            elemento.innerText = data['hello'];
        });
});