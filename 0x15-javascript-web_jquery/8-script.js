$.get(
  'https://swapi-api.alx-tools.com/api/films/?format=json',
  function (response) {
    $.each(response.results, function (_, value) {
      $('UL#list_movies').append('<li>' + value.title + '</li>');
    });
  }
);
