// script fetches character name from URL
// using JQuery API
const URL = 'https://swapi-api.alx-tools.com/api/people/5/?format=json';
$.getJSON(URL, function (data) {
  const characterName = data.name;
  $('DIV#character').text(characterName);
});
