-- lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each
SELECT genres.name, COUNT(tv_shows.id) FROM genres
JOIN tv_show_genres ON genres.id = tv_show_genres.genre_id
Group BY genres.name
ORDER BY COUNT(tv_shows.id) DESC, genres.name ASC;
