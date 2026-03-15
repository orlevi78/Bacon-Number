import pandas as pd
import sqlite3

NUMBER_OF_ROWS = 2000000

conn = sqlite3.connect("movies_and_actors.db")
cursor = conn.cursor()


def create_people_table():

    cursor.execute("CREATE TABLE IF NOT EXISTS people (nconst TEXT PRIMARY KEY, name TEXT)")
    conn.commit()
    name_basics = pd.read_csv(
        "imdb_files/name.basics.tsv", sep="\t", usecols=["nconst", "primaryName"], nrows=NUMBER_OF_ROWS
    )
    nconsts_list = list(name_basics["nconst"])
    names_list = list(name_basics["primaryName"])
    values = list(zip(nconsts_list, names_list))
    cursor.executemany("INSERT INTO people (nconst, name) VALUES (?, ?)", values)
    conn.commit()


def create_movies_table():
    cursor.execute("CREATE TABLE IF NOT EXISTS movies (tconst TEXT PRIMARY KEY, title TEXT)")
    conn.commit()
    title_basics = pd.read_csv(
        "imdb_files/title.basics.tsv", sep="\t", usecols=["tconst", "primaryTitle"], nrows=NUMBER_OF_ROWS
    )
    tconsts_list = list(title_basics["tconst"])
    titles_list = list(title_basics["primaryTitle"])
    values = list(zip(tconsts_list, titles_list))
    cursor.executemany("INSERT INTO movies (tconst, title) VALUES (?, ?)", values)
    conn.commit()


def create_transitions_tables():
    cursor.execute("CREATE TABLE IF NOT EXISTS transitions (ID INT PRIMARY KEY, tconst TEXT, nconst TEXT)")
    conn.commit()
    title_basics = pd.read_csv(
        "imdb_files/title.principals.tsv", sep="\t", usecols=["tconst", "nconst"], nrows=NUMBER_OF_ROWS
    )
    tconsts_list = list(title_basics["tconst"])
    nconst_list = list(title_basics["nconst"])
    values = list(zip([i for i in range(NUMBER_OF_ROWS)], tconsts_list, nconst_list))
    cursor.executemany("INSERT INTO transitions (ID, tconst, nconst) VALUES (?, ?, ?)", values)
    conn.commit()


def main():
    create_people_table()
    create_movies_table()
    create_transitions_tables()


if __name__ == "__main__":
    main()
