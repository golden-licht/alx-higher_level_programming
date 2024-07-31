#!/usr/bin/node

const { argv } = require('node:process');
const request = require('request');

const url = argv[2];

request(url, (err, response, body) => {
  if (err) console.error(err);
  const parsedBody = JSON.parse(body);

  const completedTasks = {};
  let id = -1;

  for (const data of parsedBody) {
    if (data.userId !== id) {
      id = data.userId;
      completedTasks[id] = 0;
    }
    if (data.completed) { completedTasks[id] += 1; }
  }

  console.log(completedTasks);
});
