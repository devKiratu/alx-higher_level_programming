#!/usr/bin/node

const request = require('request');
const fs = require('fs');

const url = process.argv[2];
const filepath = process.argv[3];

request.get(url)
  .on('error', (err) => { throw err; })
  .pipe(fs.createWriteStream(filepath));
