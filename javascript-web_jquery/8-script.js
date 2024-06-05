$.ajax({
  url: 'https://swapi-api.hbtn.io/api/films/?format=json',
  type: 'GET',
  success: function(data) {
    for (const obj of data.results) {
      const li = $('<li></li>');
      li.text(obj.title);
      $('#list_movies').append(li);
    }
  },
  error: function(xhr, status, error) {
    console.error('Error:', error);
  }
});