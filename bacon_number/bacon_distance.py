import sqlite3

from .consts import DB_NAME


def find_distance_from_bacon(name: str) -> int:
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(f"SELECT bacon_number FROM transitions WHERE nconst = '{name}'")
    ans = cursor.fetchone()[0]

    return ans
