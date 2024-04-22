#!/usr/bin/node

// Print two arguments passed to it by concatenating them with is
const { argv } = require('node:process');

console.log(`${argv[2]} is ${argv[3]}`);
