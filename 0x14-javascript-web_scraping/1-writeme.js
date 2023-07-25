#!/usr/bin/node
/* Writes a string to a file
 * If an error occurs during writing, prints the error object
 * If no error occurs, prints 'The file was saved!'
*/
const fs = require('fs');
const file = process.argv[2];
const string = process.argv[3];

fs.writeFile(process.argv[2], process.argv[3], error => {
  if (error) console.log(error);
});