#!/usr/bin/node

// Print x times “C is fun”, where x is the first argument passed
const { argv } = require('node:process');
const intValue = parseInt(argv[2], 10);

if (isNaN(intValue)) console.log('Missing number of occurrences');
else for (let i = 0; i < intValue; i++) console.log('C is fun');
