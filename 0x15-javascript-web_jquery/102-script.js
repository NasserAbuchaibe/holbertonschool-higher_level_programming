#!/usr/bin/node
$(function () {
  $('input#btn_translate').click(function () {
    const lang = $('input#language_code').val();
    const urlFull = 'https://www.fourtonfish.com/hellosalut/?lang=' + lang;
    $.getJSON(urlFull, function (body) {
      $('div#hello').text(body.hello);
    });
  });
});
