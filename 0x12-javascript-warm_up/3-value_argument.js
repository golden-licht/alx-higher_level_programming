#!/usr/bin/node

// Print the first argument passed
const { argv } = require('node:process');

if (argv[2]) console.log(argv[2]);
else console.log('No argument');
