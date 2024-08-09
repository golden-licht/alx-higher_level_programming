$(document).ready(function () {
  $('INPUT#btn_translate').click(function () {
    handleTranslation();
  });
});

function handleTranslation () {
  const langCode = $('INPUT#language_code').val();
  const langTranslateAPI = `https://hellosalut.stefanbohacek.dev/?lang=${langCode}`;

  $.get(langTranslateAPI, (data, status) => {
    $('DIV#hello').text(data.hello);
  });
}
