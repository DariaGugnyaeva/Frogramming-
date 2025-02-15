CREATE TABLE IF NOT EXISTS library (
    id INTEGER PRIMARY KEY,
    name_book TEXT,
    author TEXT,
    year_created INTEGER,
    edition INTEGER,
    num_book_case INTEGER,
    num_shell INTEGER,
    CHECK (year_created < 2026 AND name_book <> '')
);
