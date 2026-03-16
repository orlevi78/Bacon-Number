import sqlite3
import re
from .consts import DB_NAME, ID_PREFIX, PERSON_NOT_FOUND_ERROR, ID_NOT_FOUND_ERROR


def find_distance_from_bacon(name: str) -> int:
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    if input_is_name(name):
        # It's a name. Should translate it to an ID.
        cursor.execute(f"SELECT nconst FROM people WHERE name='{name}'")
        name = cursor.fetchone()
        if not name:
            return PERSON_NOT_FOUND_ERROR
        name = name[0]

    cursor.execute(f"SELECT bacon_number FROM transitions WHERE nconst = '{name}'")
    ans = cursor.fetchone()
    return ID_NOT_FOUND_ERROR if not ans else ans[0]


def input_is_name(name: str) -> bool:
    """
    nm[0-9]+ is ID. Anything else is name.
    """
    return not re.search(f"{ID_PREFIX}[0-9]+", name)
