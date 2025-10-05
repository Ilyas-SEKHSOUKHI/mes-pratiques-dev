DROP TABLE WORLD_CITY;
CREATE TABLE WORLD_CITY(
	id integer PRIMARY KEY,
	name varchar(35),
	CountryCode varchar(3),
	District varchar(20),
	Population int
);

DROP TABLE WORLD_COUNTRY;
CREATE TYPE continent_enum AS ENUM (
  'Asie',
  'Europe',
  'North America',
  'Africa',
  'Oceania',
  'Antarctica',
  'South America'
);
CREATE TABLE WORLD_COUNTRY(
	Code serial primary key,
	Name varchar(25),
	Continent continent_enum,
	Region varchar(25),
	SurfaceArea float,
	indepYear smallint,
	Population int,
	LifeExpectancy float,
	GNP float,
	LocalName varchar(45),
	GovernementForm varchar(45),
	HeadOfState varchar(60),
	Capital int,
	Code2 varchar(2)
);

DROP TABLE countrylanguage;
CREATE TYPE continent_enum2 AS ENUM(
  'T',
  'F'
);
CREATE TABLE countrylanguage (
    CountryCode VARCHAR(3),
    Language VARCHAR(30),
    isOfficial continent_enum2,
    Percentage REAL,
    PRIMARY KEY (CountryCode, Language)
);
-- A corrigé demain