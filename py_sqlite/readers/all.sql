SELECT readers.num_reader_card, visitors.surname, visitors.name, library.name_book
FROM readers
JOIN visitors
  ON visitors.num_reader_card = readers.num_reader_card
JOIN library
  ON readers.ID_book = library.id;
