#!/usr/bin/node
const argv = process.argv;

function add (a, b) {
  return a + b;
}

if (argv.length <= 2) {
  console.log('NaN');
} else {
  console.log(add(parseInt(argv[2]), parseInt(argv[3])));
}
