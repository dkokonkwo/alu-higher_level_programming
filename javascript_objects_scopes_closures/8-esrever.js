#!/usr/bin/node
exports.esrever = function (list) {
  const newList = [];
  let i = list.length;
  for (i = list.length - 1; i > -1; i--) {
    newList.push(list[i]);
  }
  return newList;
};
