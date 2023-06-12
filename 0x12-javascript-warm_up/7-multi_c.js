#!/usr/bin/node
const argv = process.argv;
const num = parseInt(argv[2]);
const string = 'C is fun';

if (isNaN(num)) {
  console.log('Missing number of occurrences');
} else {
  i = 0;
  while (i !== num) {
    console.log(string);
    i++;
  }
}
