-- schema.sql
-- Drop table if already exists
DROP TABLE IF EXISTS person CASCADE;
DROP TABLE IF EXISTS tweet CASCADE;


-- Create tables
-- Create table person
CREATE TABLE person (
    username VARCHAR PRIMARY KEY,
    name VARCHAR NOT NULL,
    picture VARCHAR NOT NULL
);

-- Create table tweet
CREATE TABLE tweet (
    username VARCHAR REFERENCES person (username) ON DELETE CASCADE,
    tweet VARCHAR,
    PRIMARY KEY (username, tweet)
);
