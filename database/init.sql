CREATE TABLE IF NOT EXISTS greetings (
    id SERIAL PRIMARY KEY,
    message VARCHAR(255) NOT NULL
);

INSERT INTO greetings (message) VALUES ('Hello Anju from Postgres Database!');
