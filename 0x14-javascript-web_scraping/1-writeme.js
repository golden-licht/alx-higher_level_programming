#!/usr/bin/node

const { argv } = require('node:process');
const fs = require('node:fs');

const fileName = argv[2];
const content = argv[3];

fs.writeFile(fileName, content, 'utf-8', (err) => {
  if (err) console.error(err);
});
