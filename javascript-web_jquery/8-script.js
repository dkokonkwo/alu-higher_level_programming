// script fetches movie title from URL
// using JQuery API
const URL = 'https://swapi-api.alx-tools.com/api/films/?format=json';
$.getJSON(URL, function (data) {
  const results = data.results;
  $.each(results, function (key, value) {
    $('UL#list_movies').append('<li>' + value.title + '</li>');
  });
});
