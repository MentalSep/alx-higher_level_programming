$('document').ready(function () {
  function getHello () {
    const langCode = $('INPUT#language_code').val();
    $.get(`https://www.fourtonfish.com/hellosalut/hello/?lang=${langCode}`, function (data) {
      $('DIV#hello').text(data.hello);
    });
  }
  $('INPUT#btn_translate').click(getHello);
  $('INPUT#language_code').keypress(function (e) {
    if (e.which === 13) {
      getHello();
    }
  });
});
