def threeNumberSum(array, targetSum):
    # Write your code here.
    results = []
    array.sort()

    for i in range(len(array) - 2):
        left_idx = i + 1
        right_idx = len(array) - 1

        while left_idx < right_idx:
            current_sum = array[i] + array[left_idx] + array[right_idx]

            if current_sum == targetSum:
                results.append(
                    [array[i],
                     array[left_idx],
                     array[right_idx]]
                )
                left_idx += 1
                right_idx -= 1

            elif current_sum < targetSum:
                left_idx += 1

            elif current_sum > targetSum:
                right_idx -= 1

    return results
