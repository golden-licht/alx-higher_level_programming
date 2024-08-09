const url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';

$(document).ready(function () {
  $.get(url, (data, status) => {
    const hello = $('DIV#hello');
    hello.text(data.hello);
    console.log(data);
  });
});
