#!/usr/bin/node
const argv = process.argv;
const num = parseInt(argv[2]);

if (isNaN(num)) {
  console.log('Missing number of occurrences');
} else {
  let i = 0;
  while (i !== num) {
    console.log('C is fun');
    i++;
  }
}
