import pytest

from problem1 import get_problem1
from problem18 import get_problem18
from problem2 import get_problem2
from problem3 import get_problem3
from problem4 import get_problem4
from problem5 import get_problem5
from problem6 import get_problem6
from problem67 import get_problem67
from problem7 import get_problem7
from problem8 import get_problem8
from problem9 import get_problem9
from problem10 import get_problem10
from problem11 import get_problem11
from problem12 import get_problem12
from problem13 import get_problem13
from problem14 import get_problem14
from problem15 import get_problem15
from problem16 import get_problem16
from problem17 import get_problem17
from problem18 import get_problem18

test_data = [
    [get_problem1, 233_168],
    [get_problem2, 4_613_732],
    [get_problem3, 6_857],
    [get_problem4, 906_609],
    [get_problem5, 232_792_560],
    [get_problem6, 25_164_150],
    [get_problem7, 104_743],
    [get_problem8, 23_514_624_000],
    [get_problem9, 31_875_000],
    [get_problem10, 142_913_828_922],
    [get_problem11, 706_00_674],
    [get_problem12, 76_576_500],
    [get_problem13, 5_537_376_230],
    [get_problem14, 837_799],
    [get_problem15, 137_846_528_820],
    [get_problem16, 1_366],
    [get_problem17, 21_124],
    [get_problem18, 1074],
    [get_problem67, 7273],
]


@pytest.mark.parametrize("data", test_data)
def test_problems(data):
    assert data[0]() == data[1]
