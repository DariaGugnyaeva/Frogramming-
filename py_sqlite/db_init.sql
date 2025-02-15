CREATE TABLE IF NOT EXISTS library (
    id INTEGER PRIMARY KEY,
    name_book VARCHAR(20),
    surname VARCHAR(50),
    author VARCHAR(25),
    year_created INTEGER,
    edition INTEGER,
    num_book_case INTEGER,
    num_shell INTEGER,
    status BOOLEAN DEFAULT FALSE,
    CHECK ((year_created < 2026) AND (name_book <> ''))
);
