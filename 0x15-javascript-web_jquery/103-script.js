#!/usr/bin/node
function translate () {
  const url = 'https://www.fourtonfish.com/hellosalut/';
  const lang = $('input#language_code').val();
  $.getJSON(url, { lang: lang }, function (body) {
    $('div#hello').text(body.hello);
  });
}

$(function () {
  $('input#btn_translate').on('click', translate);
  $('input#language_code').on('keydown', function (event) {
    if (event.keyCode === 13) {
      translate();
    }
  });
});
