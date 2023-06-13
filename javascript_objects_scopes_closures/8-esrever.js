#!/usr/bin/node
exports.esrever = function (list) {
  new_list = [];
  let i = list.length;
  for (i = list.length - 1; i > -1; i--) {
    new_list.push(list[i]);
  }
  return new_list;
}