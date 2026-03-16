from typing import Dict, List

import pandas as pd
import sqlite3

NUMBER_OF_ROWS = 10000000

visited: Dict[str, bool] = {}


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
    cursor.execute("CREATE TABLE IF NOT EXISTS transitions (nconst TEXT PRIMARY KEY, bacon_number INT)")
    conn.commit()
    title_basics = pd.read_csv(
        "/Users/orlevi/Documents/bis-projects/Bacon-Number/tests/simple_demo2.tsv",
        sep="\t",
        usecols=["tconst", "nconst"],
        # nrows=NUMBER_OF_ROWS,
    )
    tconsts_list = list(title_basics["tconst"])
    nconst_list = list(title_basics["nconst"])
    # print(tconsts_list)
    # values = list(zip([i for i in range(NUMBER_OF_ROWS)], tconsts_list, nconst_list))
    # cursor.executemany("INSERT INTO transitions (ID, tconst, nconst) VALUES (?, ?, ?)", values)
    # conn.commit()

    bacon_number = 0
    target_list = [("bacon", bacon_number)]
    colleagues = ["bacon"]
    visited["bacon"] = True
    new_colleagues: List[str] = []
    for colleague in colleagues:
        new_colleagues += find_colleagues(colleague, nconst_list, tconsts_list)
    # print(new_colleagues)
    # new_colleagues = [find_colleagues(colleague) for colleague in colleagues]
    while len(new_colleagues) > 0:
        bacon_number += 1
        target_list += ((colleague, bacon_number) for colleague in new_colleagues)
        colleagues = new_colleagues
        new_colleagues = []
        for colleague in colleagues:
            new_colleagues += find_colleagues(colleague, nconst_list, tconsts_list)

    cursor.executemany("INSERT INTO transitions (nconst, bacon_number) VALUES (?, ?)", target_list)
    conn.commit()


def find_colleagues(name: str, nconst_list, tconsts_list) -> List[str]:
    print(f"name: {name}")
    indexes = [index for index, value in enumerate(nconst_list) if value == name]
    # print(f"indexes: {indexes}")
    movies = [tconsts_list[index] for index in indexes]
    movies_indexes = [index for index, value in enumerate(tconsts_list) if value in movies]
    colleagues = [nconst_list[index] for index in movies_indexes if visited.get(nconst_list[index]) is None]
    for colleague in colleagues:
        visited[colleague] = True
    return colleagues


def create_correct_table():
    pass


def main():
    # create_people_table()
    # create_movies_table()
    create_transitions_tables()

    cursor.execute("SELECT * FROM transitions")
    print(cursor.fetchall())


if __name__ == "__main__":
    main()
