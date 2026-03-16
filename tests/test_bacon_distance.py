from math import inf
import pytest

from bacon_number import bacon_distance


# # TODO: Add  ("matt", inf) case.
# @pytest.mark.parametrize("name, expected", [("bacon", 0), ("arnold", 1), ("deamon", 2), ("will", 1)])
# def test_find_distance_from_bacon(name, expected):
#     assert bacon_distance.find_distance_from_bacon(name) == expected


@pytest.mark.parametrize("name, expected", [("nm0000102", 0), ("nm0000004", 1), ("nm0000982", 1), ("nm0000062", 2)])
def test_find_distance_from_bacon_real(name, expected):
    assert bacon_distance.find_distance_from_bacon(name) == expected
