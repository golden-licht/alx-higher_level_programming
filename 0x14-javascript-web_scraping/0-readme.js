#!/usr/bin/node

const { argv } = require('node:process');
const fs = require('node:fs');

// argv[0] and argv[1] are node's path & the scriptName
const fileName = argv[2];

fs.readFile(fileName, 'utf-8', (err, data) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(data);
});
