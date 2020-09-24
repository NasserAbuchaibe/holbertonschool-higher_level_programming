#!/usr/bin/node
$.getJSON('https://fourtonfish.com/hellosalut/?lang=fr', (data) => {
  $('#hello').append(`<p>${data.hello}</p>`);
});
