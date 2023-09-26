#!/usr/bin/node

const request = require('request');

const url = process.argv[2];
const id = 18;

request.get(url, (error, response, body) => {
  if (error) {
    throw error;
  } else if (response.statusCode === 200) {
    const data = JSON.parse(body);
    const count = data.results.reduce((acc, result) => {
      result.characters.forEach(c => {
        if (c.substr(-3, 2) === id.toString()) {
          acc += 1;
        }
      });
      return acc;
    }, 0);
    console.log(count);
  }
});
