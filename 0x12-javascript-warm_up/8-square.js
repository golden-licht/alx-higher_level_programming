#!/usr/bin/node

// Print a square of size from the frist argument passed
const { argv } = require('node:process');
const intValue = parseInt(argv[2]);
const character = 'X';

if (isNaN(intValue)) console.log('Missing size');
else for (let i = 0; i < intValue; i++) console.log(character.repeat(intValue));
