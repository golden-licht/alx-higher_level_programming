const url = 'https://swapi-api.alx-tools.com/api/films/?format=json';

$.get(url, (data, status) => {
  const ul = $('UL#list_movies');

  data.results.map((film) => {
    return ul.append(`<li>${film.title}</li>`);
  });
});
