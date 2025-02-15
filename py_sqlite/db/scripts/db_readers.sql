CREATE TABLE readers (
    id INTEGER PRIMARY KEY,
    ID_book INTEGER NOT NULL,
    num_reader_card INTEGER NOT NULL,
    FOREIGN KEY (ID_book)
        REFERENCES library(id)
    FOREIGN KEY (num_reader_card)
        REFERENCES visitors(id)
);
