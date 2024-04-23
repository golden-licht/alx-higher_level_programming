#!/usr/bin/node

// Write a function that prints the number of arguments already printed and the new argument value. (see example below)

// Prototype: exports.logMe = function (item)
// Output format: <number arguments already printed>: <current argument value>

exports.logMe = (function (item) {
  let counter = 0;

  return function printItem (item) {
    console.log(`${counter++}: ${item}`);
  };
}());
