import sqlite3

from db.utils import get_script_from_file


class Task:
    """
    Class implementing task table logic
    """

    class class_library:  # TaskObjects
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

    class class_visitors:
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

        def all(self) -> list[tuple[str, str, bool]]:
            return self._template_query("all.sql")

        def create(self, name: str, description: str) -> None:
            self._template_query("create.sql", name, description)

        def search(self, pattern: str) -> list[tuple[int, str, str, bool]]:
            return self._template_query("search.sql", pattern, pattern)

        def delete(self, id: int) -> None:
            self._template_query("delete.sql", id)

    class class_readers:
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

        def all(self) -> list[tuple[str, str, bool]]:
            return self._template_query("all.sql")

    conn: sqlite3.Connection
    objects: class_library, class_visitors, class_readers

    def __init__(self, db_path: str) -> None:
        self.conn = sqlite3.connect(db_path)
        cursor = self.conn.cursor()
        cursor.executescript(get_script_from_file("db_init.sql"))
        self.conn.commit()
        self.objects = Task.class_library(self.conn)
        self.objects = Task.class_visitors(self.conn)
        self.objects = Task.class_readers(self.conn)
