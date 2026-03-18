import sqlite3

from .generate_db import create_table, create_people_table
from .consts import DB_NAME


def main():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE name='transitions' AND type='table'")
    if cursor.fetchone() is None:
        print("Creating transitions DB.")
        create_table()
    cursor.execute("SELECT name FROM sqlite_master WHERE name='people' AND type='table'")
    if cursor.fetchone() is None:
        print("Creating people DB")
        create_people_table()


if __name__ == "__main__":
    main()
