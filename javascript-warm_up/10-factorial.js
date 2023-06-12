#!/usr/bin/node
const myArg = process.argv.slice(2);
const num1 = Number(myArg[0]);
function factorial (a) {
  if (a < 2) {
    return 1;
  } else {
    return (a * factorial(a - 1));
  }
}
if (isNaN(num1)) {
  console.log(1);
} else {
  console.log(factorial(num1));
}
