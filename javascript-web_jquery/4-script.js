// script toggles between two classes in header element
// using JQuery API
$('DIV#toggle_header').click(function () {
  if ($('header').hasClass('red')) {
    $('header').toggleClass('green');
  } else {
    $('header').toggleClass('red');
  }
});
