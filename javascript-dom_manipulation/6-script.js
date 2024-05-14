fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')

    .then(Response => Response.json())
    .then(data => {
        if (data['name']) {
            const show = document.getElementById('character');
            show.innerText = data['name'];
        }
    })
    .catch(error => console.error(error));