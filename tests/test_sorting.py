import pytest
from src.sorting import bubble_sort

def test_always_passes():
    assert True

def test_always_fails():
    assert False

@pytest.mark.parametrize(
        "input_list, expected_output",
        [
            ([], []),
            ([1], [1]),
            ([53, 351, 23, 12], [12, 23, 53, 351]),
            ([-4, -6, 1, 0, -2], [-6, -4, -2, 0, 1])
        ] 
)
def test_sorting(input_list, expected_output):
    assert bubble_sort(input_list) == expected_output
