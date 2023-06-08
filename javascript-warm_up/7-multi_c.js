#!/usr/bin/node
const myArgs = process.argv.slice(2);
const int = parseInt(myArgs[0]);
if (isNaN(int)) {
  console.log('Missing number of occurences');
} else {
    var count = 0;
    while (count < myArgs[0]) {
        console.log('C is fun');
        count++;
    }
}
