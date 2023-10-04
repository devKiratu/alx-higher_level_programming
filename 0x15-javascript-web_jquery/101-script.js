$(document).ready(function () {
  $('DIV#add_item').on('click', function () {
    $('UL.my_list').append('<li>Item</li>');
  });
  $('DIV#remove_item').on('click', function () {
    $('UL.my_list li:last-of-type').remove();
  });
  $('DIV#clear_list').on('click', function () {
    $('UL.my_list li').remove();
  });
});
