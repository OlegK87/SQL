CREATE TABLE IF NOT EXISTS genre (
	id SERIAL PRIMARY KEY,
	name VARCHAR(60) NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS singer (
	id SERIAL PRIMARY KEY,
	nickname VARCHAR(60) NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS albums (
	id SERIAL PRIMARY KEY,
	title VARCHAR(60) NOT NULL,
	year_of_release integer NOT NULL CHECK (year_of_release >= 2000 AND year_of_release <= 2021)
);
CREATE TABLE IF NOT EXISTS tracks (
	id SERIAL PRIMARY KEY,
	name VARCHAR(60) NOT NULL,
	time numeric NOT NULL CHECK (time >=1 AND time <= 10),
	albums_id INTEGER NOT NULL REFERENCES albums(id) UNIQUE
);
CREATE TABLE IF NOT EXISTS genresinger (
	genre_id INTEGER REFERENCES genre(id),
	singer_id INTEGER REFERENCES singer(id),
	CONSTRAINT pk PRIMARY KEY (genre_id, singer_id)
);
CREATE TABLE IF NOT EXISTS singeralbums (
	albums_id INTEGER REFERENCES albums(id),
	singer_id INTEGER REFERENCES singer(id),
	CONSTRAINT pk2 PRIMARY KEY (albums_id, singer_id)
);
CREATE TABLE IF NOT EXISTS compilation (
	id SERIAL PRIMARY KEY,
	title VARCHAR(60) NOT NULL,
	year_of_release integer NOT NULL
);
CREATE TABLE IF NOT EXISTS compilationtracks (
	compilation_id INTEGER REFERENCES compilation(id),
	tracks_id INTEGER REFERENCES tracks(id),
	CONSTRAINT pk3 PRIMARY KEY (compilation_id, tracks_id)
);