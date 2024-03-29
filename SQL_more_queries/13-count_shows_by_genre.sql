-- lists genre and number of show
SELECT g.name AS genre, COUNT(t.show_id) AS number_of_shows
       FROM tv_genres AS g
       LEFT JOIN tv_show_genres AS t
       ON g.id = t.genre_id
       WHERE t.show_id IS NOT NULL
       GROUP BY g.id
       ORDER BY number_of_shows DESC;
