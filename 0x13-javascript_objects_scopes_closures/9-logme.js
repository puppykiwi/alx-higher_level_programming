#!/usr/bin/node

let count = 0;
exports.logMe = function (str) {
  //console.log(count + ' : ' + str);
  console.log(`${count}: ${str}`);
  count+=1;
};
