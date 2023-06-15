#!/usr/bin/node
const request = require('request');
const myArg = process.argv.slice(2);
const urlString = 'https://swapi-api.alx-tools.com/api/films/' + myArg[0];
request(urlString, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    const characters = JSON.parse(body).characters;
    let i = 0;
    for (i = 0; i < characters.length; i++) {
      const urlCharacter = characters[i];
      request(urlCharacter, function (err, response, body) {
        if (err) {
          console.log(err);
        } else {
          console.log(JSON.parse(body).name);
        }
      });
    }
  }
});
