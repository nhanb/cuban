import os
import sqlite3

songs_dir = 'songs'

def init_db(db='playlist.sqlite3'):
    db_exists = os.path.isfile(db)
    conn = sqlite3.connect(db)

    if not db_exists:
        c = conn.cursor()
        c.execute('''
        CREATE TABLE filenames (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            time_added TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            filename TEXT UNIQUE
        );
        ''')
        conn.commit()

    return conn


def add_song(conn, filename):
    assert filename, 'Filename must not be empty'
    c = conn.cursor()
    c.execute('INSERT INTO filenames (filename) VALUES (?);', (filename,))
    conn.commit()

def pop_song(conn):
    c = conn.cursor()
    c.execute('SELECT filename FROM filenames ORDER BY time_added LIMIT 1;')
    result = c.fetchone()

    if result is None:
        return 'whitenoise.ogg'

    filename = result[0]
    c = conn.cursor()
    c.execute('DELETE FROM filenames WHERE filename=?;', (filename,))
    conn.commit()
    return filename
