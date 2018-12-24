#!/usr/bin/env python3
from core import init_db, pop_song

if __name__ == "__main__":
    conn = init_db()
    next_filename = pop_song(conn)
    conn.close()
    print(f'{next_filename}')
