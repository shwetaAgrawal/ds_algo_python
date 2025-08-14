"""
BDD-style tests for Algo101/Search/binary_search.py using pytest.

Scenarios covered:
- Element present at start, middle, end
- Element absent (below-range, interior-missing, single-element missing)
- Empty list
- Single-element present
- Duplicates (any matching index acceptable)
"""

import pytest

from algo101.search.binary_search import binary_search


@pytest.mark.parametrize(
    "arr,target,expected_index",
    [
        # Given a sorted list and the target is at the beginning
        ([1, 2, 3, 4, 5], 1, 0),
        # Given a sorted list and the target is in the middle
        ([1, 2, 3, 4, 5], 3, 2),
        # Given a sorted list and the target is at the end
        ([1, 2, 3, 4, 5], 5, 4),
        # Given a single-element list containing the target
        ([7], 7, 0),
    ],
)
def test_binary_search_element_present(arr: list[int], target: int, expected_index: int):
    # Given a sorted array and a target in the array
    # When we perform binary search
    result = binary_search(arr, target)
    # Then we get the correct index of the target
    assert result == expected_index


@pytest.mark.parametrize(
    "arr,target",
    [
        # Given a sorted list where the target is below the range
        ([1, 2, 3, 4, 5], 0),
        # Given an interior non-existent value in a larger-gapped list
        ([0, 10, 20, 30, 40, 50], 35),
        # Given a non-existent value above the range
        ([0, 10, 20, 30, 40, 50], 55),
        # Given a single-element list without the target
        ([7], 8),
    ],
)
def test_binary_search_element_absent(arr: list[int], target: int):
    # Given a sorted array and a target not in the array
    # When we perform binary search
    result = binary_search(arr, target)
    # Then we get -1 indicating not found
    assert result == -1


def test_binary_search_empty_list_returns_minus_one():
    # Given an empty list
    arr: list[int] = []
    target = 42
    # When we perform binary search
    result = binary_search(arr, target)
    # Then we get -1 indicating not found
    assert result == -1


def test_binary_search_duplicates_any_matching_index():
    # Given a sorted list with duplicates
    arr = [1, 2, 2, 2, 3]
    target = 2
    # When we perform binary search
    idx = binary_search(arr, target)
    # Then we get an index that points to a matching element (any duplicate is acceptable)
    assert idx in {1, 2, 3}
    assert arr[idx] == target
