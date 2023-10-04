/*
    using https://hellosalut.stefanbohacek.dev/ as
    https://www.fourtonfish.com/hellosalut/hello/ has moved permanently to this address
    */

$(document).ready(function () {
  $('INPUT#btn_translate').on('click', function () {
    const lang = $('INPUT#language_code').val();
    const url = `https://hellosalut.stefanbohacek.dev/?lang=${lang}`;
    $.get(url, function (response) {
      $('DIV#hello').text(response.hello);
    });
  });
  $('INPUT#language_code').keypress(function (event) {
    const keycode = event.keyCode ? event.keyCode : event.which;
    if (keycode == '13') {
      const lang = $(this).val();
      const url = `https://hellosalut.stefanbohacek.dev/?lang=${lang}`;
      $.get(url, function (response) {
        $('DIV#hello').text(response.hello);
      });
    }
  });
});
