// script fetches and prints 'hello' depending on language
// using JQuery API
$(document).ready(function () {
  $('INPUT#btn_translate').click(function () {
    const URL = 'https://www.fourtonfish.com/hellosalut/hello/';
    const lang = URL + $('INPUT#language_code').val();
    $.getJSON(lang, function (data) {
      $('DIV#hello').text(data.hello);
    });
  });
});
