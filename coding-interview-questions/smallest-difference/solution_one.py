def smallestDifference(arrayOne, arrayTwo):
    # Find the pair of numbers (one from each array)
    # whose absolute difference is closest to zero
    # Return an array containing these two numbers
    arrayOne.sort()
    arrayTwo.sort()

    smallest_difference = float('inf')
    list_smallest_difference = []

    for value in arrayTwo:
        left_idx = 0
        right_idx = len(arrayOne) - 1

        while left_idx <= right_idx:
            if (abs(arrayOne[left_idx] - value) < smallest_difference):
                list_smallest_difference = [arrayOne[left_idx], value]
                smallest_difference = abs(arrayOne[left_idx] - value)

            if (abs(arrayOne[right_idx] - value) < smallest_difference):
                list_smallest_difference = [arrayOne[right_idx], value]
                smallest_difference = abs(arrayOne[right_idx] - value)

            left_idx += 1
            right_idx -= 1

    return list_smallest_difference
