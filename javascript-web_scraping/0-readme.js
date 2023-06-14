#!/usr/bin/node
const fs = require('fs');
const myArg = process.argv.slice(2);
// scripts reads and prints contents of a file
fs.readFile(myArg[0], 'utf8', function (err, data) {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
});
