INSERT INTO singer
VALUES (1, 'AC/DC'), (2, 'Scorpions'), (3, 'Linkin Park'), (4, 'Offspring'), (5, 'Green Day'), (6, 'Metallica'), (7, 'Red Hot Chilli Peppers'), (8, 'Jay-Z');
INSERT INTO genre
VALUES (1, 'Rock'), (2, 'Alternative'), (3, 'Punk-Rock'), (4, 'Metal'), (5, 'Rap');
INSERT INTO albums
VALUES (1, 'Stiff Upper Lip', 2000), (2, 'Sting In The Tail', 2010), (3, 'Meteora', 2003), (4, 'Conspiracy of One', 2000), (5, 'Revolution Radio', 2018), (6, 'St. Anger', 2003), (7, 'The Getaway', 2016), (8, 'Kingdom Come', 2006), (9, 'Splinter', 2003), (10, 'Power Up', 2020), (11, 'Father of All…', 2020), (12, 'Hybrid Theory', 2000);
INSERT INTO tracks
VALUES (1, 'Stiff Upper Lip', 3.34, 1), (2, 'Give It Up', 3.54, 1), (3, 'Raised on Rock', 4.00, 2), (4, 'The Best Is Yet to Come', 4.32, 2), (5, 'Faint', 2.42, 3), (6, 'Numb', 3.08, 3), (7, 'Million Miles Away', 3.40, 4), (8, 'Original Prankster', 3.41, 4), (9, 'Somewhere Now', 4.08, 5), (10, 'Say Goodbye', 3.39, 5), (11, 'Frantic', 5.50, 6), (12, 'Some Kind of Monster', 8.26, 6), (13, 'The Getaway', 4.10, 7), (14, 'Dark Necessities', 5.02, 7), (15, 'Kingdom Come', 4.23, 8), (16, 'Hollywood', 4.17, 8), (17, '(Can’t Get My) Head Around You', 2.14, 9), (18, 'Hit That', 2.50, 9), (19, 'Realize', 3.37, 10), (20, 'Rejection', 4.06, 10), (21, 'Father of All…', 2.31, 11), (22, 'Fire, Ready, Aim', 1.52, 11), (23, 'House of Jazz', 3.56, 1), (24, 'Rock Zone', 3.17, 2), (25, 'One Step Closer', 2.36, 12);
INSERT INTO genresinger 
VALUES (1, 1), (1, 2), (2, 3), (3, 4), (3, 5), (4, 6), (1, 7), (5, 8);
INSERT INTO singeralbums 
VALUES (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 4), (10, 1), (11, 5), (12, 3);
INSERT INTO compilation 
VALUES (1, 'Best of Rock', 2019), (2, 'Best of Rock', 2019), (3, 'Best of Rock', 2020), (4, 'Best of Rock', 2020), (5, 'Best of Rock', 2020), (6, 'Best of Alternative and Rap', 2021), (7, 'Best of Alternative and Rap', 2021), (8, 'Best of Alternative and Rap', 2021), (9, 'Best of Metal and Punk-Rock', 2022), (10, 'Best of Metal and Punk-Rock', 2022), (11, 'Best of Metal and Punk-Rock', 2022), (12, 'Best of Metal and Punk-Rock', 2022);
INSERT INTO compilationtracks
VALUES (1, 1), (2, 3), (2, 4), (7, 13), (7, 14), (3, 5), (3, 6), (8, 15), (6, 11), (6, 12), (4, 7), (5, 10);