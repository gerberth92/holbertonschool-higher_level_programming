fetch('https://swapi-api.hbtn.io/api/films/?format=json')

    .then(Response => Response.json())
    .then(data => {
        for (let di of data['results']) {
            const elemento = document.getElementById('list_movies');
            const nuevo = document.createElement('li');
            nuevo.innerText = di['title'];
            elemento.appendChild(nuevo);
        }
    })
    .catch(error => console.error(error));