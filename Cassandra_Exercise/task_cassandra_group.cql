CREATE KEYSPACE videogamesdb
WITH replication = {'class': 'SimpleStrategy', 'replication_factor' : 1};

USE videogamesdb;

CREATE TABLE users ( 
	name VARCHAR,
	facebook_account VARCHAR,
	nationality VARCHAR,
	birthdate TIMESTAMP,
	logister_date TIMESTAMP,	
	PRIMARY KEY (facebook_account)
);

CREATE TABLE videogames_by_user_date ( 
	facebook_account VARCHAR,
	buy_date TIMESTAMP,
	title VARCHAR,	
	PRIMARY KEY ((facebook_account),buy_date)
)WITH CLUSTERING ORDER BY (buy_date DESC);

CREATE TABLE videogames ( 
	id UUID,
	title VARCHAR,
	description VARCHAR,
	genre SET<VARCHAR>,
	min_age INT,
	release_date TIMESTAMP,
	PRIMARY KEY ((id), min_age, release_date)
)WITH CLUSTERING ORDER BY (min_age ASC,release_date ASC);

/* 
 INSERTS
 * 
COPY users (facebook_account,name,birthdate,nationality,logister_date) 
from '/home/master/Descargas/usr.csv' with header = 'true';
* 
COPY videogames_by_user_date (title, facebook_account, buy_date)
from '/home/master/Descargas/videogames_by_user_date.csv' with header = 'true';
* 
COPY videogames (id,title,description,release_date,min_age,genre) 
from '/home/master/Descargas/videogames.csv' with header = 'true';

*/

SELECT buy_date, title
FROM videogames_by_user_date
WHERE facebook_account = 'Frank_E_Graham';

SELECT *
FROM videogames
WHERE min_age >= 18
ALLOW FILTERING;