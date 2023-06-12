#!/usr/bin/node
const argv = process.argv;
let length = 0;
while (argv[length] !== undefined) { length++; }

if (length === 2) {
  console.log('No argument');
} else {
  console.log(argv[2]);
}
