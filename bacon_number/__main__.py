import sqlite3

from .bacon_distance import find_distance_from_bacon
from .generate_db import create_table, create_people_table
from .consts import DB_NAME


def main():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE name='transitions'")
    if cursor.fetchone() is None:
        print("Creating transitions DB.")
        create_table()
    cursor.execute("SELECT name FROM sqlite_master WHERE name='people'")
    if cursor.fetchone() is None:
        print("Creating people DB")
        create_people_table()

    name = input("Please enter the name of the person you wish to search for\n")
    bacon_number = find_distance_from_bacon(name)
    if bacon_number == -1:
        print(f"Error! Person: '{name}' is unknown.")
    elif bacon_number == -2:
        print(f"Error! ID: {name} is unkown.")
    else:
        print(f"Bacon number of '{name}' is: {bacon_number}")


if __name__ == "__main__":
    main()
