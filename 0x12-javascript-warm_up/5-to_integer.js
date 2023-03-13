#!/usr/bin/node
const argv = process.argv;
if (Number.isInteger(Number(argv[2])) === true) {
  console.log('My number: ' + argv[2]);
} else {
  console.log('Not a number');
}
