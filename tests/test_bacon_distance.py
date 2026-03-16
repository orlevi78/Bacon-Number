from math import inf
import pytest

from bacon_number import bacon_distance
from bacon_number.consts import ID_NOT_FOUND_ERROR, PERSON_NOT_FOUND_ERROR


@pytest.mark.parametrize(
    "name, expected",
    [
        ("nm0000102", 0),  # Kevin Bacon
        ("nm0000004", 1),  # John Belushi
        ("nm0000982", 1),  # Josh Brolin
        ("nm0000062", 2),  # Elvis Presley
        ("nm1", ID_NOT_FOUND_ERROR),
        ("nm2395670", inf),
        ("Gal Gadot", 2),
        ("Kevin Bacon", 0),
        ("Hilary Farr", 3),
        ("Mister obviously I dont exist", PERSON_NOT_FOUND_ERROR),
    ],
)
def test_find_distance_from_bacon(name, expected):
    assert bacon_distance.find_distance_from_bacon(name) == expected
