#!/usr/bin/node
const argv = process.argv;
const num = parseInt(argv[2]);

if (isNaN(num) || num < 0) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i !== num; i++) {
    let s = '';
    for (let j = 0; j !== num; j++) {
      s += 'X';
    }
    console.log(s);
  }
}
