#!/usr/bin/node
const myArgs = process.argv.slice(2);
if (myArgs.length === 0 || myArgs.length === 1) {
  console.log(0)
} else {
  let i = 0;
  let max = 0;
  let max_2 = 0;
  if (Number(myArgs[0]) > Number(myArgs[1])) {
    max = myArgs[0];
    max_2 = myArgs[1];
  } else {
    max = myArgs[1];
    max_2 = myArgs[0];
  }
  for (i = 2; i < myArgs.length; i++) {
    if (Number(myArgs[i]) > max) {
      max_2 = max;
      max = myArgs[i];
    } else if (Number(myArgs[i]) < max && Number(myArgs[i]) > max_2) {
      max_2 = myArgs[i];
    }
  }
  console.log(max_2)
}
