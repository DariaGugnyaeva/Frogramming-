SELECT
    name,
    surname,
    num_reader_card
FROM visitors
WHERE (name LIKE '%' || ? || '%') OR (surname LIKE '%' || ? || '%') OR (num_reader_card = ?);
