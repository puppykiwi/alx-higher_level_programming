#!/usr/bin/node
/* prints out the name of a Star Wars episode by its id */

const request = require('request');
const id = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + id;

request(url, function (err, response, body) {
  if (err) {
    return console.log(err);
  }
  console.log(JSON.parse(body).title);
});
