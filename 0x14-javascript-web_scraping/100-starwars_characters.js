#!/usr/bin/node

const request = require('request');

const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

request.get(url, (error, response, data) => {
  if (error) {
    throw error;
  } else {
    const film = JSON.parse(data);
    film.characters.forEach(character => {
      request.get(character, (error, response, data) => {
        if (error) {
          throw error;
        } else {
          const filmChar = JSON.parse(data);
          console.log(filmChar.name);
        }
      });
    });
  }
});
