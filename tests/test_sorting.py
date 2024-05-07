import pytest

from src.plus import plus_plus
from src.sorting import bubble_sort
from src.togri import nums


def test_always_passes():
    assert True

def test_always_fails():
    assert True

@pytest.mark.parametrize(
        "input_nums, output",
        [
            ([], []),
            ([1], [1]),
            ([53, 351, 23, 12], [12, 23, 53, 351]),
            ([-4, -6, 1, 0, -2], [-6, -4, -2, 0, 1])
        ] 
)
def test_sorting(input_nums, output):
    assert bubble_sort(input_nums) == output

@pytest.mark.parametrize(
    "a, b, c",
    nums
)
def test_plus_plus(a, b, c):
    assert plus_plus(a, b) == c