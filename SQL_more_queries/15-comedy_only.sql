-- hm
SELECT tv_shows.title 
FROM tv_shows
INNER JOIN tv_genre_shows ON tv_shows.id = tv_genre_shows.show_id
INNER JOIN tv_genres ON tv_genre_shows.genre_id = tv_genres.id
WHERE tv_genres.name = 'Comedy'
ORDER BY tv_shows.title ASC;
