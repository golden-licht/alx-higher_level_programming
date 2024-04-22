#!/usr/bin/node

// Compute factorial of a number
function factorial (num) {
  if (isNaN(num) || num <= 1) return 1;
  return (num * factorial(num - 1));
}

const { argv } = require('node:process');
const intValue = parseInt(argv[2], 10);
console.log(factorial(intValue));
