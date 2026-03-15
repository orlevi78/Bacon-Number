from copy import deepcopy
import math
from typing import Dict, List
import sqlite3

visited: Dict[str, bool] = {}
distances: Dict[str, int] = {}


def find_distance_from_bacon(name: str) -> int:
    if name == "nm0000102":
        distances[name] = 0
        return 0

    dist = distances.get(name)
    if dist is not None:
        print("save time")
        return dist
    # print("here")

    colleagues: List[str] = find_colleagues(name)
    # print(len(colleagues))
    colleagues_not_visited = deepcopy(colleagues)
    for colleauge in colleagues:
        if visited.get(colleauge) is not None:
            # print("visited")
            colleagues_not_visited.remove(colleauge)
        else:
            visited[colleauge] = True
    if len(colleagues_not_visited) == 0:
        distances[name] = math.inf
        return math.inf

    return 1 + min(find_distance_from_bacon(colleague) for colleague in colleagues_not_visited)


def find_colleagues(name: str) -> List[str]:
    conn = sqlite3.connect("movies_and_actors.db")
    cursor = conn.cursor()
    cursor.execute(f"SELECT tconst FROM transitions WHERE nconst = '{name}'")  # Seems like a big smell. Fix it.
    movies = list(set(cursor.fetchall()))  # Done to remove duplicates.
    # print(f"name: {name}")
    # print(f"movies: {movies}")
    colleagues: List[str] = []
    for movie in movies:
        movie = movie[0]
        cursor.execute(f"SELECT nconst FROM transitions WHERE tconst = '{movie}'")
        colleagues += list(set(cursor.fetchall()))
    colleagues_formated = [item[0] for item in colleagues]
    # colleagues_formated.remove(name)
    return colleagues_formated


# print(find_distance_from_bacon("nm0342399"))
print(find_distance_from_bacon("nm0000982"))
