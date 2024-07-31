#!/usr/bin/node

const { argv } = require('node:process');
const request = require('request');

const url = 'https://swapi-api.alx-tools.com/api/films/' + argv[2];

request(url, (err, response, body) => {
  if (err) console.error(err);
  const parsedBode = JSON.parse(body);
  console.log(parsedBode.title);
});
