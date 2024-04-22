#!/usr/bin/node

// Add two numbers
function add (a, b) {
  return a + b;
}

const { argv } = require('node:process');
const result = add(parseInt(argv[2], 10), parseInt(argv[3], 10));
console.log(result);
