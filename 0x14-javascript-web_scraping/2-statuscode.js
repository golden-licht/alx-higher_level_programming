#!/usr/bin/node

const { argv } = require('node:process');
const request = require('request');

const url = argv[2];

request(url, (err, response, body) => {
  console.log('code: ', response.statusCode);
});
