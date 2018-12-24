#!/usr/bin/env python3
from core import init_db, pop_song, songs_dir

if __name__ == "__main__":
    conn = init_db()
    next_filename = pop_song(conn)
    conn.close()
    print(f'{songs_dir}/{next_filename}')
