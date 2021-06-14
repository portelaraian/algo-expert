# O(nlogn) Time | O(1) Space
# where n is the length of the array
def sortedSquaredArray(array):
    right_idx = len(array) - 1
    left_idx = 0

    while left_idx <= right_idx:
        array[left_idx] = array[left_idx] ** 2

        # Ensure only one square applied when the indexes
        # (left and right) are equal.
        if (left_idx != right_idx):
            array[right_idx] = array[right_idx] ** 2

        left_idx += 1
        right_idx -= 1

    array.sort()
    return array
