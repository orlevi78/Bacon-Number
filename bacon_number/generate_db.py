from typing import Dict, List

import pandas as pd
import sqlite3

from collections import defaultdict

from consts import DB_NAME, BACON_NAME, NUMBER_OF_ROWS_TO_READ, PATH_TO_DATA


visited: Dict[str, bool] = {}

people_to_movies: Dict[str, List[str]] = defaultdict(list)
movies_to_people: Dict[str, List[str]] = defaultdict(list)


def create_table():

    title_basics = pd.read_csv(
        PATH_TO_DATA,
        sep="\t",
        usecols=["tconst", "nconst"],
        nrows=NUMBER_OF_ROWS_TO_READ,
    )
    tconsts_list = list(title_basics["tconst"])
    nconst_list = list(title_basics["nconst"])

    for i in range(len(tconsts_list)):
        person_name = nconst_list[i]
        movie_name = tconsts_list[i]
        movies_to_people[movie_name].append(person_name)
        people_to_movies[person_name].append(movie_name)

    bacon_number = 0
    target_list = [(BACON_NAME, bacon_number)]
    colleagues = [BACON_NAME]
    visited[BACON_NAME] = True
    new_colleagues: List[str] = []
    for colleague in colleagues:
        new_colleagues += find_colleagues(colleague, nconst_list, tconsts_list)
    while len(new_colleagues) > 0:
        print("started iteration")
        print(len(new_colleagues))
        # print(new_colleagues)
        bacon_number += 1
        target_list += ((colleague, bacon_number) for colleague in new_colleagues)
        colleagues = new_colleagues
        new_colleagues = []
        for colleague in colleagues:
            new_colleagues += find_colleagues(colleague, nconst_list, tconsts_list)

    print(f"target list: {target_list}")

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS transitions (nconst TEXT PRIMARY KEY, bacon_number INT)")
    conn.commit()
    cursor.executemany("INSERT INTO transitions (nconst, bacon_number) VALUES (?, ?)", target_list)
    conn.commit()


num = 0


def find_colleagues(name: str, nconst_list, tconsts_list) -> List[str]:
    global num
    # print(num)
    num += 1
    movies = people_to_movies[name]
    colleagues = []
    for movie in movies:
        colleagues += [person for person in movies_to_people[movie] if visited.get(person) is None]
    for colleague in colleagues:
        visited[colleague] = True
    return colleagues


def main():
    create_table()


if __name__ == "__main__":
    main()
