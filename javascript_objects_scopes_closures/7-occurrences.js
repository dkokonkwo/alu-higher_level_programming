#!/usr/bin/node
exports.nbOccurences = function nbOccurences (list, searchElement) {
  let i = 0;
  let count = 0;
  for (i = 0; i < list.length; i++) {
    if (list[i] === searchElement) {
      count += 1;
    }
  }
  return count;
};