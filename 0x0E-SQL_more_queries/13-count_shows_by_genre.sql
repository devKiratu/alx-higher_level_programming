-- This script lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.
-- A genre that doesn’t have any shows linked is not displayed
-- Results are sorted in descending order by the number of shows linked
SELECT tg.name AS genre, count(*) AS number_of_shows
FROM tv_genres tg
JOIN tv_show_genres tsg 
ON tg.id = tsg.genre_id 
GROUP BY genre
ORDER BY number_of_shows DESC;
