-- This script lists all Comedy shows in the database hbtn_0d_tvshows.
-- Results are sorted in ascending order by the show title
SELECT ts.title
FROM tv_shows ts
JOIN tv_show_genres tsg
ON ts.id = tsg.show_id
JOIN tv_genres tg
ON tsg.genre_id = tg.id
WHERE tg.name = 'Comedy'
ORDER BY ts.title;
