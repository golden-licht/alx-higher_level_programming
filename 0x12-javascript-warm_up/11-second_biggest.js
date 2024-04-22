#!/usr/bin/node

function findSecondBiggestInt (arr) {
  // convert each memeber to int
  const intArr = arr.map((element) => parseInt(element, 10));
  let biggest = intArr[0];
  let secondBiggest = intArr[1];

  for (let i = 1; i < intArr.length; i++) {
    if (intArr[i] > secondBiggest && intArr[i] < biggest) {
      secondBiggest = intArr[i];
    } else if (intArr[i] >= biggest) {
      secondBiggest = biggest;
      biggest = intArr[i];
    }
  }

  return secondBiggest;
}

const { argv } = require('node:process');
if (argv.length === 2 || argv.length === 3) console.log(0);
else console.log(findSecondBiggestInt(argv.slice(2)));
