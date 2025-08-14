"""Recursive quick sort algorithm implementation."""

from random import randint


def randomize_pivot(arr: list, low: int, high: int, partition_style="Lomuto"):
    """Randomly select a pivot and move it to a boundary position.

    Args:
        arr (list): The array to partition.
        low (int): The starting index of the partition.
        high (int): The ending index of the partition.
    """
    pivot = randint(low, high)

    # move pivot to the end
    if partition_style == "Lomuto" and pivot != high:
        arr[pivot], arr[high] = arr[high], arr[pivot]
    elif partition_style == "Hoare" and pivot != low:
        arr[pivot], arr[low] = arr[low], arr[pivot]


def quick_sort(arr: list, reverse: bool = False) -> list:
    """Sort a list using quick sort.

    Args:
        arr (list): A list of elements to sort.
        reverse (bool): If True, sort in descending order; otherwise, ascending.

    Returns
    -------
        list: The sorted list.
    """
    if len(arr) < 2:
        return arr

    len_arr, pivot, last_idx = len(arr), len(arr) - 1, 0
    randomize_pivot(arr, 0, len_arr - 1)

    # we don't iterate on last element as that is our pivot
    for idx in range(len_arr - 1):
        if (not reverse and arr[idx] < arr[pivot]) or (reverse and arr[idx] > arr[pivot]):
            if idx != last_idx:
                arr[idx], arr[last_idx] = arr[last_idx], arr[idx]
            last_idx += 1

    # finally swap last_idx and pivot
    arr[pivot], arr[last_idx] = arr[last_idx], arr[pivot]
    # Recursively apply quick_sort to the partitions
    left = quick_sort(arr[:last_idx], reverse)
    right = quick_sort(arr[last_idx + 1 :], reverse)
    return left + [arr[last_idx]] + right


def quick_sort_inplace(
    arr: list, reverse: bool = False, low: int = 0, high: int | None = None
) -> list:
    """Sort a list in place using quick sort.

    Args:
        arr (list): A list of elements to sort.
        reverse (bool): If True, sort in descending order; otherwise, ascending.
        low (int): The starting index for the sort.
        high (int): The ending index for the sort.

    Returns
    -------
        list: The sorted list.
    """
    if len(arr) < 2 or (high is not None and low >= high):
        return arr

    high = len(arr) - 1 if high is None else high
    pivot, last_idx = high, low
    randomize_pivot(arr, low, high)

    # we don't iterate on last element as that is our pivot
    for idx in range(low, high):
        if (not reverse and arr[idx] < arr[pivot]) or (reverse and arr[idx] > arr[pivot]):
            if idx != last_idx:
                arr[idx], arr[last_idx] = arr[last_idx], arr[idx]
            last_idx += 1

    # finally swap last_idx and pivot
    arr[pivot], arr[last_idx] = arr[last_idx], arr[pivot]
    # Recursively apply quick_sort to the partitions
    quick_sort_inplace(arr, reverse, low, last_idx - 1)
    quick_sort_inplace(arr, reverse, last_idx + 1, high)
    return arr


def quick_sort_hoare(arr: list, reverse: bool = False) -> list:
    """Sort a list using quick sort with Hoare partition.

    Args:
        arr (list): The array to partition.
        reverse (bool): If True, sort in descending order; otherwise, ascending.

    Returns
    -------
        list: The sorted list.
    """
    if len(arr) < 2:
        return arr

    randomize_pivot(arr, 0, len(arr) - 1, "Hoare")
    pivot_val, left_idx, right_idx = arr[0], -1, len(arr)
    while True:
        left_idx, right_idx = left_idx + 1, right_idx - 1
        while (not reverse and arr[left_idx] < pivot_val) or (
            reverse and arr[left_idx] > pivot_val
        ):
            left_idx += 1
        while (not reverse and arr[right_idx] > pivot_val) or (
            reverse and arr[right_idx] < pivot_val
        ):
            right_idx -= 1
        if left_idx >= right_idx:
            break
        arr[left_idx], arr[right_idx] = arr[right_idx], arr[left_idx]
    left_arr = quick_sort_hoare(arr[: right_idx + 1], reverse)
    right_arr = quick_sort_hoare(arr[right_idx + 1 :], reverse)
    return left_arr + right_arr


def quick_sort_hoare_inplace(
    arr: list, reverse: bool = False, low: int = 0, high: int | None = None
) -> list:
    """Sort a list in place using quick sort with Hoare partition.

    Args:
        arr (list): The array to partition.
        reverse (bool): If True, sort in descending order; otherwise, ascending.
        low (int): The starting index for the sort.
        high (int): The ending index for the sort.

    Returns
    -------
        list: The sorted list.
    """
    if len(arr) < 2 or (high is not None and low >= high):
        return arr

    high = len(arr) - 1 if high is None else high
    randomize_pivot(arr, low, high, "Hoare")
    pivot_val, left_idx, right_idx = arr[low], low - 1, high + 1
    while True:
        left_idx, right_idx = left_idx + 1, right_idx - 1
        while (not reverse and arr[left_idx] < pivot_val) or (
            reverse and arr[left_idx] > pivot_val
        ):
            left_idx += 1
        while (not reverse and arr[right_idx] > pivot_val) or (
            reverse and arr[right_idx] < pivot_val
        ):
            right_idx -= 1
        if left_idx >= right_idx:
            break
        arr[left_idx], arr[right_idx] = arr[right_idx], arr[left_idx]
    quick_sort_hoare_inplace(arr, reverse, low, right_idx)
    quick_sort_hoare_inplace(arr, reverse, right_idx + 1, high)
    return arr
