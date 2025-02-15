SELECT
    name,
    surname,
    num_reader_card
FROM visitors
WHERE (name LIKE '%' || ? || '%') OR (second_name LIKE '%' || ? || '%') OR (num_reader_card = ?);
