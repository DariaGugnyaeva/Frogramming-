CREATE TABLE readers (
    id INTEGER PRIMARY KEY,
    ID_book,
    num_reader_card,
    FOREIGN KEY (ID_book)
        REFERENCES library(id)
    FOREIGN KEY (num_reader_card)
        REFERENCES visitors(id)
);
