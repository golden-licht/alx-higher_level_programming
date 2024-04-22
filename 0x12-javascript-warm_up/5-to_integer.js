#!/usr/bin/node

// Convert the first argument to integer
const { argv } = require('node:process');
const intValue = parseInt(argv[2], 10);

if (!isNaN(intValue)) console.log(`My number: ${intValue}`);
else console.log('Not a number');
