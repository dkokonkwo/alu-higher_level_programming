#!/usr/bin/node
let count = 0;
exports.logMe = function (some) {
  console.log(count + ': ' + some);
  count++;
};
