SELECT name, COUNT(nickname) FROM genre e -- 1 . количество исполнителей в каждом жанре;
JOIN genresinger g ON e.id = g.genre_id
JOIN singer s ON s.id = singer_id
GROUP BY name
ORDER BY COUNT(nickname);
SELECT COUNT(name), year_of_release FROM tracks t -- 2 . количество треков, вошедших в альбомы 2019-2020 годов;
LEFT JOIN albums a ON t.albums_id = a.id
WHERE (a.year_of_release >= 2019) AND (a.year_of_release <= 2020)
GROUP BY year_of_release
ORDER BY COUNT(name);
SELECT AVG(time), title FROM tracks t -- 3 . средняя продолжительность треков по каждому альбому;
LEFT JOIN albums a ON t.albums_id = a.id
GROUP BY a.title;
SELECT DISTINCT nickname FROM singer s -- 4 . все исполнители, которые не выпустили альбомы в 2020 году;
WHERE nickname NOT IN (SELECT DISTINCT nickname FROM singer s 
LEFT JOIN singeralbums i ON s.id = i.singer_id 
LEFT JOIN albums a ON a.id = albums_id
WHERE year_of_release  = 2020)
ORDER BY nickname;
SELECT o.title, o.year_of_release, nickname FROM tracks t -- 5 . названия сборников, в которых присутствует конкретный исполнитель (выберите сами);
JOIN compilationtracks c ON t.id = c.tracks_id
JOIN compilation o ON o.id = compilation_id
JOIN albums a ON a.id = t.albums_id
JOIN singeralbums s ON s.albums_id = a.id
JOIN singer s2 ON s2.id = s.singer_id
WHERE nickname LIKE 'Scorpions';
SELECT COUNT(*), title FROM genre e -- 6 . название альбомов, в которых присутствуют исполнители более 1 жанра;
JOIN genresinger g ON e.id = g.genre_id
JOIN singer s ON s.id = singer_id
JOIN singeralbums s2 ON s.id = s2.singer_id
JOIN albums a ON a.id = s2.albums_id
GROUP BY title
HAVING COUNT(*) > 1
ORDER BY COUNT(*);
SELECT name, title FROM tracks t -- 7 . наименование треков, которые не входят в сборники;
LEFT JOIN compilationtracks c ON t.id = c.tracks_id
LEFT JOIN compilation o ON o.id = compilation_id
WHERE title IS NULL;
SELECT name, time, nickname FROM tracks t -- 8 . исполнителя(-ей), написавшего самый короткий по продолжительности трек (теоретически таких треков может быть несколько)
LEFT JOIN albums a ON a.id = t.albums_id
JOIN singeralbums i ON a.id = i.albums_id 
JOIN singer s ON s.id = i.singer_id
WHERE time = (SELECT (MIN(time)) FROM tracks);
SELECT a.title FROM albums a -- 9 . название альбомов, содержащих наименьшее количество треков.
JOIN tracks t ON a.id = t.albums_id
GROUP BY a.title
HAVING COUNT(*) = (SELECT MIN(county) FROM albums a
JOIN (SELECT a2.title, a2.id, COUNT(*) AS "county" FROM albums a2
JOIN tracks t ON a2.id = t.albums_id
GROUP BY a2.title, a2.id) m ON a.id = m.id)
ORDER BY COUNT(*);
