#!/usr/bin/node
const myArgs = process.argv.slice(2);
if (myArgs.length === 0 || myArgs.length === 1) {
  console.log(0);
} else {
  let i = 0;
  let max = 0;
  let maxt = 0;
  if (Number(myArgs[0]) > Number(myArgs[1])) {
    max = myArgs[0];
    maxt = myArgs[1];
  } else {
    max = myArgs[1];
    maxt = myArgs[0];
  }
  for (i = 2; i < myArgs.length; i++) {
    if (Number(myArgs[i]) > max) {
      maxt = max;
      max = myArgs[i];
    } else if (Number(myArgs[i]) < max && Number(myArgs[i]) > maxt) {
      maxt = myArgs[i];
    }
  }
  console.log(maxt);
}
