$(document).ready(function () {
  $('INPUT#btn_translate').on('click', function () {
    const lang = $('INPUT#language_code').val();
    /*
    using https://hellosalut.stefanbohacek.dev/ as
    https://www.fourtonfish.com/hellosalut/hello/ has moved permanently
    */
    const url = `https://hellosalut.stefanbohacek.dev/?lang=${lang}`;
    $.get(url, function (response) {
      $('DIV#hello').text(response.hello);
    });
  });
});
