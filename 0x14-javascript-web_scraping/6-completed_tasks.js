#!/usr/bin/node
/* a script that computes the number of tasks completed by user id */

const request = require('request');
const url = process.argv[2];
const dict = {};

request(url, function (err, response, body) {
  if (err) {
    return console.log(err);
  }
  const results = JSON.parse(body);
  for (const task of results) {
    if (task.completed === true) {
      if (task.userId in dict) {
        dict[task.userId]++;
      } else {
        dict[task.userId] = 1;
      }
    }
  }
  console.log(dict);
}
);
