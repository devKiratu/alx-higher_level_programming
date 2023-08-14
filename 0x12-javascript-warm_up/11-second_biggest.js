#!/usr/bin/node

const args = process.argv;

if (args.length <= 3) {
  console.log(0);
} else {
  let first = parseInt(args[2], 10);
  let second = Number.MIN_VALUE;

  for (let i = 3; i < args.length; i++) {
    const num = parseInt(args[i]);
    if (num > first) {
      second = first;
      first = num;
    } else if (num > second) {
      second = num;
    }
  }
  console.log(second);
}
