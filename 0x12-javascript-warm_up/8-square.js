#!/usr/bin/node
const argv = process.argv;
const num = parseInt(argv[2]);
if (isNaN(num)) {
  console.log('Missing size');
}

for (i = 0; i < num; i++) {
  let row = '';
  for (j = 0; j < num; j++) {
    row += 'x';
  }
  console.log(row);
}
