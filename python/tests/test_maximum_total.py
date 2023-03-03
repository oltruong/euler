import os

from lib.maximum_total import find_maximum_total


def test_find_maximum_total():
    assert find_maximum_total([
        [3, ],
        [7, 4, ],
        [2, 4, 6, ],
        [8, 5, 9, 3],
    ]) == 23
