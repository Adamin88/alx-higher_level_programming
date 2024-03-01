def find_peak(list_of_integers):
    """
    Finds a peak in a list of unsorted integers.

    Args:
    - list_of_integers: A list of unsorted integers

    Returns:
    - peak: A peak element in the list
    """
    # Helper function to check if an element is a peak
    def is_peak(arr, index):
        if index == 0:
            return arr[index] >= arr[index + 1]
        elif index == len(arr) - 1:
            return arr[index] >= arr[index - 1]
        else:
            return arr[index] >= arr[index - 1] and arr[index] >= arr[index + 1]

    # Binary search for peak
    left, right = 0, len(list_of_integers) - 1
    while left < right:
        mid = (left + right) // 2
        if is_peak(list_of_integers, mid):
            return list_of_integers[mid]
        elif list_of_integers[mid] < list_of_integers[mid + 1]:
            left = mid + 1
        else:
            right = mid

    # Return the remaining element (if the list length is 1)
    return list_of_integers[left]

# Example usage:
# list_of_integers = [1, 3, 5, 7, 10, 6, 4]
# print(find_peak(list_of_integers))
