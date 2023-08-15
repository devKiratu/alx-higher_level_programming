#!/usr/bin/node

exports.esrever = function (list) {
  let temp;
  let j = list.length - 1;

  for (let i = 0; i < j; i++) {
    temp = list[i];
    list[i] = list[j];
    list[j] = temp;
    j--;
  }

  return list;
};
