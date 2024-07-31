#!/usr/bin/node

const { argv } = require('node:process');
const request = require('request');

const url = argv[2];

request(url, (err, response, body) => {
  if (err) console.error(err);
  console.log('code:', response.statusCode);
});
