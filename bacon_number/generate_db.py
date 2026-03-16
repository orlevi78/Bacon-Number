from typing import Dict, List

import pandas as pd
import sqlite3

from consts import DB_NAME, BACON_NAME, NUMBER_OF_ROWS_TO_READ, PATH_TO_DATA


visited: Dict[str, bool] = {}


conn = sqlite3.connect(DB_NAME)
cursor = conn.cursor()


def create_table():
    cursor.execute("CREATE TABLE IF NOT EXISTS transitions (nconst TEXT PRIMARY KEY, bacon_number INT)")
    conn.commit()
    title_basics = pd.read_csv(
        PATH_TO_DATA,
        sep="\t",
        usecols=["tconst", "nconst"],
        # nrows=NUMBER_OF_ROWS,
    )
    tconsts_list = list(title_basics["tconst"])
    nconst_list = list(title_basics["nconst"])

    bacon_number = 0
    target_list = [(BACON_NAME, bacon_number)]
    colleagues = [BACON_NAME]
    visited[BACON_NAME] = True
    new_colleagues: List[str] = []
    for colleague in colleagues:
        new_colleagues += find_colleagues(colleague, nconst_list, tconsts_list)
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
    indexes = [index for index, value in enumerate(nconst_list) if value == name]
    movies = [tconsts_list[index] for index in indexes]
    movies_indexes = [index for index, value in enumerate(tconsts_list) if value in movies]
    colleagues = [nconst_list[index] for index in movies_indexes if visited.get(nconst_list[index]) is None]
    for colleague in colleagues:
        visited[colleague] = True
    return colleagues


def main():
    create_table()


if __name__ == "__main__":
    main()
