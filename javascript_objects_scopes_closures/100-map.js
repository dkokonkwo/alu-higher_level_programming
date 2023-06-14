#!/usr/bin/node
const testList = require('./100-data').list;
let mp = new Map();
let newList = [];
// split list into key and value
let i = 0;
for (i = 0; i < testList.length; i++) {
  mp.set(testList[i], i);
}
// multipy and add the new array
for (let entry of mp) {
  newList.push(entry[0] * entry[1]);
}
console.log(testList);
console.log(newList);