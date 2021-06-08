# O(n) Time | O(1) Space
def moveElementToEnd(array, toMove):
    right_idx = len(array) - 1
    left_idx = 0

    while left_idx < right_idx:
        while (array[right_idx] == toMove) and (left_idx < right_idx):
            right_idx -= 1

        if array[left_idx] == toMove:
            aux = array[right_idx]
            array[right_idx] = array[left_idx]
            array[left_idx] = aux

            left_idx += 1
            right_idx -= 1
        else:
            left_idx += 1

    return array
