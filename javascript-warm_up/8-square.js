#!/usr/bin/node
const myArgs = process.argv.slice(2);
const myVar = 'X';
const num = Number(myArgs[0]);
if (isNaN(num)) {
  console.log("Missing size");
} else {
    let i = 0;
    string = '';
    for (i = 0; i < num; i++) {
      string += myVar;
    }
    for (i = 0; i < num; i++) {
      console.log(string);
    }
}
