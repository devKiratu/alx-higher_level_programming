#!/usr/bin/node

const dict = require('./101-data.js').dict;

const sorted = {};

for (const [key, value] of Object.entries(dict)) {
  if (Object.keys(sorted).includes(value.toString())) {
    sorted[value].push(key);
  } else {
    sorted[value] = [key];
  }
}
console.log(sorted);
