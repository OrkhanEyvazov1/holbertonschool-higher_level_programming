-- dexter morgan , The Bay Harbour Butcher
SELECT tv_genre.name
FROM tv_genre
INNER JOIN tv_shows_genres ON tv_genres.id = tv_shows_genres.genre_id
INNER JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
WHERE tv_shows.title = 'Dexter';
ORDER BY tv_genres.name ASC;
