#!/usr/bin/node

const { argv } = require('node:process');
const fs = require('node:fs');
const request = require('request');

const url = argv[2];
const fileName = argv[3];

request(url, (err, response, body) => {
  if (err) console.error(err);

  fs.writeFile(fileName, body, 'utf-8', (err) => {
    if (err) console.error(err);
  });
});
