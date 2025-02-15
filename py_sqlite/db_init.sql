CREATE TABLE IF NOT EXISTS library (
    id INTEGER PRIMARY KEY,
    name_book VARCHAR(20) NOT NULL,
    surname VARCHAR(50) NOT NULL,
    author VARCHAR(25) NOT NULL,
    year_created INTEGER,
    edition INTEGER,
    num_book_case INTEGER NOT NULL,
    num_shell INTEGER NOT NULL,
    status BOOLEAN DEFAULT FALSE,
    CHECK (year_created < 2026)
);
