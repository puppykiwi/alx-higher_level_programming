#!/usr/bin/node

/*
* script that prints all characters of a Star Wars movie:
* The first argument is the Movie ID - example: 3 = “Return of the Jedi”
* Display one character name by line in the same order of the list “characters” in the /films/ response
*/

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
