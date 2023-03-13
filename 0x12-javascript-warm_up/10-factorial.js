#!/usr/bin/node
const argv = process.argv;

function fact (a) {
  if (isNaN(a) || a === 1) {
    return 1;
  } else {
    return a * fact(a - 1);
  }
}

console.log(fact(parseInt(argv[2])));
