/*show databases ;*/ --Pour Afficher les databases existe dans le pc n’existe pas dans PostgreSQL
CREATE DATABASE Test ; --Pour Cree une DB
--show databases ;
/*USE Test ; */    --Pour utiliser la BD n’existe pas dans PostgreSQL
/*SHOW TABLES ; */ --Pour afficher les table de ma BD n’existe pas dans PostgreSQL


DROP TABLE Premiere_table;
CREATE TABLE Premiere_table( --Cree une table
	id SERIAL PRIMARY KEY , --Colonne auto-incrémentée
	name varchar(25), --Chaine de caractères
	ville varchar(25) --ville
/*	Heure Time, --heure
	LaDate Date --date*/
);

INSERT INTO Premiere_table (name, ville) VALUES ('test', 'test1');

/*describe Premiere_table;*/ --Pour afficher la discription de la table n’existe pas dans PostgreSQL

