"""
BDD-style tests for sorting algorithms using pytest.

We feed the same scenarios to multiple implementations to ensure consistent
behavior: selection_sort, quick_sort (Lomuto), and quick_sort_hoare.

Scenarios covered:
- Ascending and descending sorts on typical input
- Empty and single-element lists
- Duplicates
- Already sorted and reverse-sorted inputs
- Negative numbers and mixed values
- In-place behavior test only for selection_sort (it mutates input)
"""

import pytest

from algo101.sorting.quick_sort import (
    quick_sort,
    quick_sort_hoare,
    quick_sort_hoare_inplace,
    quick_sort_inplace,
)
from algo101.sorting.selection_sort import selection_sort

# A matrix of sorter functions to apply across shared scenarios
SORTERS = [
    pytest.param(selection_sort, id="selection_sort"),
    pytest.param(quick_sort, id="quick_sort_lomuto"),
    pytest.param(quick_sort_hoare, id="quick_sort_hoare"),
    pytest.param(quick_sort_inplace, id="quick_sort_inplace"),
    pytest.param(quick_sort_hoare_inplace, id="quick_sort_hoare_inplace"),
]


@pytest.mark.parametrize("sorter", SORTERS)
def test_sort_ascending_basic(sorter):
    # Given an unsorted list
    arr = [64, 25, 12, 22, 11]
    # When we sort ascending
    result = sorter(arr.copy())
    # Then we get ascending order
    assert result == [11, 12, 22, 25, 64]


@pytest.mark.parametrize("sorter", SORTERS)
def test_sort_descending_basic(sorter):
    # Given an unsorted list
    arr = [3, 1, 4, 1, 5, 9]
    # When we sort descending
    result = sorter(arr.copy(), reverse=True)
    # Then the list is sorted in descending order
    assert result == [9, 5, 4, 3, 1, 1]


@pytest.mark.parametrize("sorter", SORTERS)
def test_sort_empty_and_singleton(sorter):
    # Given an empty list
    empty: list[int] = []
    # When sorted
    assert sorter(empty.copy()) == []
    # Given a single-element list
    one = [42]
    # When sorted
    assert sorter(one.copy()) == [42]


@pytest.mark.parametrize("sorter", SORTERS)
@pytest.mark.parametrize(
    "arr,expected",
    [
        # Already sorted ascending remains the same
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
        # Reverse sorted becomes ascending
        ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
        # Mixed negatives and positives
        ([0, -1, -3, 2, 1], [-3, -1, 0, 1, 2]),
        # Duplicates present
        ([2, 2, 1, 1, 3], [1, 1, 2, 2, 3]),
    ],
)
def test_sort_varied_inputs(sorter, arr: list[int], expected: list[int]):
    # Given various lists
    # When sorted ascending
    result = sorter(arr.copy())
    # Then result matches expected sorted content
    assert result == expected


@pytest.mark.parametrize("sorter", SORTERS)
@pytest.mark.parametrize(
    "arr,expected",
    [
        # sorted ascending becomes descending
        ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]),
        # Already sorted descending remains the same
        ([5, 4, 3, 2, 1], [5, 4, 3, 2, 1]),
        # Mixed negatives and positives
        ([0, -1, -3, 2, 1], [2, 1, 0, -1, -3]),
        # Duplicates present
        ([2, 2, 1, 1, 3], [3, 2, 2, 1, 1]),
    ],
)
def test_sort_descending_parametrized(sorter, arr: list[int], expected: list[int]):
    # Given various lists
    # when reverse sorted
    result = sorter(arr.copy(), reverse=True)
    # Then it matches expected
    assert result == expected


def test_selection_sort_in_place_behavior():
    # Given an input list
    original = [4, 2, 5, 1, 3]
    # When sorting ascending
    result = selection_sort(original)
    # Then the same object is mutated and returned
    assert result is original
    assert original == [1, 2, 3, 4, 5]
