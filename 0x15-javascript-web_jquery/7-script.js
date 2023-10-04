$.get(
  'https://swapi-api.alx-tools.com/api/people/5/?format=json',
  function (response) {
    console.log(response);
    $('DIV#character').text(response.name);
  }
);
