from math import inf
import pytest

from bacon_number import bacon_distance


# TODO: Add  ("matt", inf) case.
@pytest.mark.parametrize("name, expected", [("bacon", 0), ("arnold", 1), ("deamon", 2), ("will", 1)])
def test_find_distance_from_bacon(name, expected):
    assert bacon_distance.find_distance_from_bacon(name) == expected
