#!/usr/bin/node

const fs = require('fs');

const file1 = process.argv[2];
const file2 = process.argv[3];
const filed = process.argv[4];

fs.readFile(file1, (err, data) => {
  if (err) {
    console.log(err);
  } else {
    fs.appendFile(filed, data, (err) => {
      if (err) console.log(err);
    });
  }
});

fs.readFile(file2, (err, data) => {
  if (err) {
    console.log(err);
  } else {
    fs.appendFile(filed, data, (err) => {
      if (err) console.log(err);
    });
  }
});
