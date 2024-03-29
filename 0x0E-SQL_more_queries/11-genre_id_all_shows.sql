-- This script lists all shows contained in hbtn_0d_tvshows that have at least one genre linked or none.
SELECT ts.title, tsg.genre_id
FROM tv_shows ts 
LEFT JOIN tv_show_genres tsg 
ON ts.id = tsg.show_id 
ORDER BY ts.title, tsg.genre_id;
