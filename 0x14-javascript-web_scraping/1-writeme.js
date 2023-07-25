#!/usr/bin/node
/* Writes a string to a file
 * If an error occurs during writing, prints the error object
 * If no error occurs, prints 'The file was saved!'
*/
const fs = require('fs');
const file = process.argv[2];
const string = process.argv[3];
fs.writeFile(file, string, 'utf8', function (err) {
  if (err) {
    return console.log(err);
  }
  console.log('The file was saved!');
});
