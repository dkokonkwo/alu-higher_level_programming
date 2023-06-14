#!/usr/bin/node
const request = require('request');
const myArg = process.argv.slice(2);
const urlString = 'https://swapi-api.alx-tools.com/api/films/:id' + myArg[0];
request(urlString, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    console.log(JSON.parse(body).title);
  }
});
