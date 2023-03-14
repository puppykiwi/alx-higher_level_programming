#!/usr/bin/node

exports.esrever = function (list) {
  const tmp = [];
  let j = list.length - 1;
  for (let i = 0; i !== list.length; i++) {
    tmp[i] = list[j];
    j--;
  }
  return tmp;
};
