#!/usr/bin/node

const request = require('request');

request(process.argv[2], function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    const data = JSON.parse(body);
    const len = data.length;

    const dict = {};

    for (let x = 0; x < len; x++) {
      if (data[x].completed) {
        if (!(data[x].userId in dict)) {
          dict[data[x].userId] = 0;
        }
        dict[data[x].userId] += 1;
      }
    }
    console.log(dict);
  }
});
