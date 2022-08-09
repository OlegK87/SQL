SELECT title, year_of_release FROM albums -- 1. название и год выхода альбомов, вышедших в 2018 году;
WHERE year_of_release = 2018;
SELECT name, time FROM tracks -- 2. название и продолжительность самого длительного трека;
WHERE time = (SELECT (MAX(time)) FROM tracks);
SELECT name, time FROM tracks -- 3. название треков, продолжительность которых не менее 3,5 минуты;
WHERE time >= 3.30;
SELECT title, year_of_release FROM compilation -- 4. названия сборников, вышедших в период с 2018 по 2020 год включительно;
WHERE  year_of_release BETWEEN 2018 AND 2020;
SELECT nickname FROM singer -- 5. исполнители, чье имя состоит из 1 слова;
WHERE nickname NOT LIKE '% %';
SELECT name FROM tracks -- 6. название треков, которые содержат слово "мой"/"my".
WHERE name LIKE '%My%' OR name LIKE '%Мой%';

