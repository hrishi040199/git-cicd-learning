
from calculations import (
    calculate_total,
    calculate_average,
    calculate_minimum,
    find_maximum
)


def test_calculate_total():
    assert calculate_total([100, 200, 300]) == 600


def test_calculate_average():
    assert calculate_average([100, 200, 300]) == 200


def test_calculate_average_empty_list():
    assert calculate_average([]) == 0


def test_calculate_minimum():
    assert calculate_minimum([100, 200, 300]) == 100


def test_calculate_minimum_empty_list():
    assert calculate_minimum([]) is None


def test_find_maximum():
    assert find_maximum([100, 200, 300]) == 300
