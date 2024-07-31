#!/usr/bin/node

const { argv } = require('node:process');
const request = require('request');

const wedgeAntillesId = 18;
const wedgeAntillesURL = `https://swapi-api.alx-tools.com/api/people/${wedgeAntillesId}/`;
const filmAPI = argv[2];

request(filmAPI, (err, response, body) => {
  if (err) console.error(err);
  const parsedBody = JSON.parse(body);
  const results = parsedBody.results;

  let count = 0;
  for (const result of results) {
    const characters = result.characters;
    for (const character of characters) {
      if (character === wedgeAntillesURL) count++;
    }
  }

  console.log(count);
});
