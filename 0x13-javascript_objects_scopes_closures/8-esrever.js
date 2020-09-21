#!/usr/bin/node

exports.esrever = function (list) {
  const reverseList = [];
  let rev = 0;
  for (let count = list.length - 1; count >= 0; count--, rev++) {
    reverseList[rev] = list[count];
  }
  return reverseList;
};
