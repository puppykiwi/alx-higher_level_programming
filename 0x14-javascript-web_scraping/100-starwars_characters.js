#!/usr/bin/node
/* prints out the character name of a Star Wars movie by its id */

const request = require('request');
const id = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + id;

request(url, function (err, response, body) {
  if (err) {
    return console.log(err);
  }
  const characters = JSON.parse(body).characters;
  for (const character of characters) {
    request(character, function (err, response, body) {
      if (err) {
        return console.log(err);
      }
      console.log(JSON.parse(body).name);
    });
  }
});
