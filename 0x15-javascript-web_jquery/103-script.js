$(document).ready(function () {
  $('INPUT#btn_translate').click(function () {
    handleTranslation();
  });

  $('INPUT#language_code').keydown(function (event) {
    // checking if the key pressed is 'enter' key
    if (event.keyCode === 13) {
      handleTranslation();
    }
  });
});

function handleTranslation () {
  const langCode = $('INPUT#language_code').val();
  const langTranslateAPI = `https://hellosalut.stefanbohacek.dev/?lang=${langCode}`;

  $.get(langTranslateAPI, (data, status) => {
    $('DIV#hello').text(data.hello);
  });
}
