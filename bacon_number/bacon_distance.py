import sqlite3

from .consts import DB_NAME, PERSON_NOT_FOUND_ERROR, ID_NOT_FOUND_ERROR


def find_distance_from_bacon(name: str) -> int:
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    if not name.startswith("nm"):
        # It's a name. Should translate it to an ID.
        cursor.execute(f"SELECT nconst FROM people WHERE name='{name}'")
        name = cursor.fetchone()
        if name is None:
            return PERSON_NOT_FOUND_ERROR
        name = name[0]

    cursor.execute(f"SELECT bacon_number FROM transitions WHERE nconst = '{name}'")
    ans = cursor.fetchone()
    if ans is None:
        # Person isn't in database.
        return ID_NOT_FOUND_ERROR
    return ans[0]
