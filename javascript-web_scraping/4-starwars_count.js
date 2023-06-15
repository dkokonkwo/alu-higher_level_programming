#!/usr/bin/node
// scripts counts the number of movies “Wedge Antilles” is present
const myArg = process.argv.slice(2);
const request = require('request');
let count = 0;
request(myArg[0], function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    const results = JSON.parse(body).results;
    let i = 0;
    for (i = 0; i < results.length; i++) {
      let u = 0;
      const characters = results[i].characters;
      for (u = 0; u < characters.length; u++) {
        if (characters[u].includes('18')) {
          count += 1;
        }
      }
    }
    console.log(count);
  }
});
