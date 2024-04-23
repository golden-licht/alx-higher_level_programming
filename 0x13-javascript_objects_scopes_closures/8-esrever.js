#!/usr/bin/node

// Write a function that returns the reversed version of a list:

// Prototype: exports.esrever = function (list)
// You are not allow to use the built-in method reverse

exports.esrever = function (list) {
  const len = list.length;
  for (let i = 0; i < len / 2; i++) {
    [list[i], list[len - 1 - i]] = [list[len - 1 - i], list[i]];
  }

  return list;
};
