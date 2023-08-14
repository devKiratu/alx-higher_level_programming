#!/usr/bin/node

const num = parseInt(process.argv[2], 10);

if (isNaN(num)) {
  console.log(1);
} else {
  console.log(factorial(num));
}

function factorial (num) {
  if (num === 1) {
    return 1;
  }
  return num * factorial(num - 1);
}
