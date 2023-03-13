#!/usr/bin/node
const argv = process.argv;
const arr = [];

for (let i = 2; i !== argv.length; i++) {
  arr[i] = parseInt(argv[i]);
}
console.log(arr);
arr.sort().reverse();
console.log(arr);
console.log(arr[2]);
