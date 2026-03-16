import sqlite3

from .bacon_distance import find_distance_from_bacon
from .generate_db import create_table
from .consts import DB_NAME


def main():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE name='transitions'")
    if cursor.fetchone() is None:
        print("Please wait for us to create the DB...")
        create_table()

    name = input("Please enter the name of the person you with to search for\n")
    bacon_number = find_distance_from_bacon(name)
    print(f"Bacon number of {name} is: {bacon_number}")


if __name__ == "__main__":
    main()
