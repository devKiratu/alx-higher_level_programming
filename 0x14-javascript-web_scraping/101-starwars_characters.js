#!/usr/bin/node

const request = require('request');

const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

request.get(url, async (error, response, data) => {
  if (error) {
    throw error;
  } else {
    const film = JSON.parse(data);
    const peopleUrls = film.characters;
    for (const personUrl of peopleUrls) {
      const person = await getPersonData(personUrl);
      console.log(person.name);
    }
  }
});

const getPersonData = (personUrl) => (
  new Promise((resolve, reject) => {
    request.get(personUrl, (error, response, data) => {
      if (error) {
        reject(error);
      } else {
        const person = JSON.parse(data);
        resolve(person);
      }
    });
  })
);
