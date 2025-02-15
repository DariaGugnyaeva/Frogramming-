SELECT
    name_book,
    author,
    year_created,
    edition,
    num_book_case,
    num_shell,
    status
FROM library
WHERE (name_book LIKE '%' || ? || '%') OR (author LIKE '%' || ? || '%') OR (year_created = ?);
