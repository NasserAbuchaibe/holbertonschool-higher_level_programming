#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let ocu = 0;
  for (let count = 0; count < list.length; count++) {
    if (list[count] === searchElement) {
      ocu++;
    }
  }
  return ocu;
};
