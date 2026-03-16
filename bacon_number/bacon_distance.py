import sqlite3


def find_distance_from_bacon(name: str) -> int:
    conn = sqlite3.connect("/Users/orlevi/Documents/bis-projects/Bacon-Number/movies_and_actors.db")
    cursor = conn.cursor()

    cursor.execute(f"SELECT bacon_number FROM transitions WHERE nconst = '{name}'")
    ans = cursor.fetchone()[0]

    return ans
