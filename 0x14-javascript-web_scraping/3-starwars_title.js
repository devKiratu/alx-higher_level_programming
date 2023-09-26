#!/usr/bin/node

const request = require('request');

const id = process.argv[2];

const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

request.get(url, (error, response, body) => {
  if (error) { throw error; } else {
    const data = JSON.parse(body);
    if (data.title) {
      console.log(data.title);
    }
  }
});
