// adds <li> element to a list when the tag is
// clicked on using JQuery API
$('DIV#add_item').click(function () {
  $('UL.my_list').append('<li>Item</li>');
});
