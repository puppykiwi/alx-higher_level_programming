#!/usr/bin/node
const argv = process.argv;
function fact (n) {
  if (isNaN(n)) {
    return 1;
  }
  if (n === 1) {
    return 1;
  } else {
    return n * fact(n - 1);
  }
}
console.log(fact(parseInt(argv[2])));
