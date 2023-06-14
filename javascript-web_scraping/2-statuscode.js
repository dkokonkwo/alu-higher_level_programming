#!/usr/bin/node
// prints out the request status code
const request = require('request');
const myArg = process.argv.slice(2);
request(myArg[0], function (err, reponse) {
  if (err) {
    console.log(err);
  } else {
    console.log('code: ' + response.StatusCode);
  }
});