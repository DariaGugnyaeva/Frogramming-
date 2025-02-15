SELECT
    name,
    second_name,
    num_reader_card
FROM task
WHERE (name LIKE '%' || ? || '%') OR (second_name LIKE '%' || ? || '%') OR (num_reader_card LIKE '%' || ? || '%');
