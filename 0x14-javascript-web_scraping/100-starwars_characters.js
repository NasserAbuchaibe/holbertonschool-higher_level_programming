#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    const filmData = JSON.parse(body);
    for (const character of filmData.characters) {
      request(character, function (err, response, body) {
        if (err) {
          console.log(err);
        } else {
          const charData = JSON.parse(body);
          console.log(charData.name);
        }
      });
    }
  }
});
