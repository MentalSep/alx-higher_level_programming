#!/usr/bin/node
const request = require('request');

const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    const characters = JSON.parse(body).characters;
    printNames(characters, 0);
  }
});

function printNames (characters, index) {
  if (index >= characters.length) {
    return;
  }
  request(characters[index], function (err, response, body) {
    if (!err) {
      console.log(JSON.parse(body).name);
      printNames(characters, index + 1);
    }
  });
}
