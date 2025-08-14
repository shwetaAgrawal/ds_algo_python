"""Binary Search Algorithm Implementation."""

from typing import Any


def binary_search(arr: list, target: Any) -> int:
    """Return the index of ``target`` in a sorted list using binary search.

    If the element is present, an index is returned; otherwise ``-1`` is
    returned. In the presence of duplicates, any matching index may be
    returned.
    """
    start, end = 0, len(arr) - 1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return -1
