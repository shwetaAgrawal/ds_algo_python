"""Selection sort algorithm implementation."""


def selection_sort(arr: list[int], reverse: bool = False) -> list[int]:
    """Perform an in-place selection sort on a list.

    Args:
        arr (list): A list of elements to sort.
        reverse (bool): If True, sort in descending order; otherwise, ascending.

    Returns
    -------
        list: The sorted list.
    """
    len_arr = len(arr)
    for idx in range(len_arr):
        min_idx = idx
        for jdx in range(idx + 1, len_arr):
            if not reverse and arr[jdx] < arr[min_idx]:
                min_idx = jdx
            elif reverse and arr[jdx] > arr[min_idx]:
                min_idx = jdx
        # Swap the found minimum element with the first element
        if min_idx != idx:
            # Swap only if a new minimum was found
            arr[idx], arr[min_idx] = arr[min_idx], arr[idx]
    return arr
