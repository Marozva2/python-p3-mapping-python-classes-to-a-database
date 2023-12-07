from config import CONN, CURSOR


class Song:
    def __init__(self, name, album):
        self.id = None
        self.name = name
        self.album = album

    @classmethod
    def create_table(cls):
        sql = """
                CREATE TABLE IF NOT EXISTS songs (
                id INTEGER PRIMARY KEY,
                name TEXT,
                album TEXT
                )
            """

        try:
            CURSOR.execute(sql)
            CONN.commit()
        except Exception as e:
            print(f"Error creating table: {e}")
            CONN.rollback()

    def save(self):
        sql = """
                INSERT INTO songs (name, album)
                VALUES (?, ?)  
            """

        try:
            CURSOR.execute(sql, (self.name, self.album))
            self.id = CURSOR.lastrowid
            CONN.commit()
        except Exception as e:
            print(f"Error saving song: {e}")
            CONN.rollback()

        self.id = CURSOR.execute(
            "SELECT last_insert_rowid() FROM songs").fetchone()[0]

    @classmethod
    def create(cls, name, album):
        song = Song(name, album)
        song.save()
        return song
