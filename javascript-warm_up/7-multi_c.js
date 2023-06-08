#!/usr/bin/node
const myArgs = process.argv.slice(2);
const int = parseInt(myArgs[0]);
if (isNaN(int)) {
  console.log('Missing number of occurences');
} else {
  let i = 0;
  for (i = 0; i < int; i++) {
    console.log('C is fun');
  }
}
