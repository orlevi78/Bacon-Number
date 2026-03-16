import sqlite3

from .bacon_distance import find_distance_from_bacon
from .generate_db import create_table, create_people_table
from .consts import DB_NAME, PERSON_NOT_FOUND_ERROR, ID_NOT_FOUND_ERROR


def main():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE name='transitions' AND type='table'")
    if cursor.fetchone() is None:
        print("Creating transitions DB.")
        create_table()
    cursor.execute("SELECT name FROM sqlite_master WHERE name='people'")
    if cursor.fetchone() is None:
        print("Creating people DB")
        create_people_table()

    name = input("Please enter the name of the person you wish to search for, or their id as written in IMDB\n")
    bacon_number = find_distance_from_bacon(name)
    if bacon_number == PERSON_NOT_FOUND_ERROR:
        print(f"Error! Person: '{name}' is unknown.")
    elif bacon_number == ID_NOT_FOUND_ERROR:
        print(f"Error! ID: {name} is unkown.")
    else:
        print(f"Bacon number of '{name}' is: {bacon_number}")


if __name__ == "__main__":
    main()
