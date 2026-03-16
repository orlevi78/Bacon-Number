from math import inf
import sqlite3
import pytest


# TODO: Add  ("matt", inf) case.
@pytest.mark.parametrize("name, expected", [("bacon", 0), ("arnold", 1), ("deamon", 2), ("will", 1)])
def test_bacon_number(name, expected):
    conn = sqlite3.connect("/Users/orlevi/Documents/bis-projects/Bacon-Number/movies_and_actors.db")
    cursor = conn.cursor()

    cursor.execute(f"SELECT bacon_number FROM transitions WHERE nconst = '{name}'")
    ans = cursor.fetchone()
    print(f"Ans: {ans}")

    assert ans[0] == expected
