$(document).ready(function () {
  $.ajax({
    url: 'https://hellosalut.stefanbohacek.dev/?lang=fr',
    type: 'GET',
    success: function (response) {
      $('DIV#hello').text(response.hello);
    }
  });
});
