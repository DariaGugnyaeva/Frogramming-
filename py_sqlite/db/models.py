import sqlite3

from db.utils import get_script_from_file


class Library:
    """
    Class implementing task table logic
    """

    class ClassLibrary:  # TaskObjects
        """
        Proxy class for task table
        """

        conn: sqlite3.Connection

        def __init__(self, conn: sqlite3.Connection) -> None:
            self.conn = conn

        def _template_query(self, script: str, *args) -> list[tuple]:
            cursor = self.conn.cursor()
            script = get_script_from_file(f"task_library_db/{script}")
            res = cursor.execute(script, args)
            self.conn.commit()
            return res.fetchall()

        def all(self) -> list[tuple[str, str, bool]]:
            return self._template_query("all.sql")

        def create(self, name: str, description: str) -> None:
            self._template_query("create.sql", name, description)

        def search(self, pattern: str) -> list[tuple[int, str, str, bool]]:
            return self._template_query("search.sql", pattern, pattern)

        def complete(self, id: int) -> None:
            self._template_query("complete.sql", id)

        def delete(self, id: int) -> None:
            self._template_query("delete.sql", id)

    class ClassVisitors:
        """
        Proxy class for task table
        """

        conn: sqlite3.Connection

        def __init__(self, conn: sqlite3.Connection) -> None:
            self.conn = conn

        def _template_query(self, script: str, *args) -> list[tuple]:
            cursor = self.conn.cursor()
            script = get_script_from_file(f"visitors/{script}")
            res = cursor.execute(script, args)
            self.conn.commit()
            return res.fetchall()

        def all(self) -> list[tuple[str, str, str, int, str]]:
            return self._template_query("all.sql")

        def create(self, name: str, surname: str, second_name: str, num_reader_card: str, address: str) -> None:
            self._template_query("create.sql", name, description)

        def search(self, name: str, surname: str, num_reader_card: int) -> list[tuple[int, str, str, bool]]:
            return self._template_query("search.sql", pattern, pattern)

        def delete(self, id: int) -> None:
            self._template_query("delete.sql", id)

    class ClassReaders:
        """
        Proxy class for task table
        """

        conn: sqlite3.Connection

        def __init__(self, conn: sqlite3.Connection) -> None:
            self.conn = conn

        def _template_query(self, script: str, *args) -> list[tuple]:
            cursor = self.conn.cursor()
            script = get_script_from_file(f"readers/{script}")
            res = cursor.execute(script, args)
            self.conn.commit()
            return res.fetchall()

        def all(self) -> list[tuple[int, str, str, str, bool]]:
            return self._template_query("all.sql")

    conn: sqlite3.Connection
    objects: ClassLibrary, ClassVisitors, ClassReaders

    def __init__(self, db_path: str) -> None:
        self.conn = sqlite3.connect(db_path)
        cursor = self.conn.cursor()
        cursor.executescript(get_script_from_file("db_library.sql"))
        cursor.executescript(get_script_from_file("db_visitors.sql"))
        cursor.executescript(get_script_from_file("db_readers.sql"))
        self.conn.commit()
        self.objects_1 = Library.ClassLibrary(self.conn)
        self.objects_2 = Library.ClassVisitors(self.conn)
        self.objects_3 = Library.ClassReaders(self.conn)
