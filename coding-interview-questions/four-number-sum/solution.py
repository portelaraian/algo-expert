# O(n³) time | O(n) space
# where n is the length of the array
def fourNumberSum(array, targetSum):
    results = []
    array.sort()

    for i in range(len(array) - 3):
        for j in range(i + 1, len(array) - 2):
            left_idx = j + 1
            right_idx = len(array) - 1

            while left_idx < right_idx:
                current_sum = array[i] + array[j] + \
                    array[left_idx] + array[right_idx]

                if current_sum == targetSum:
                    results.append([
                        array[i],
                        array[j],
                        array[left_idx],
                        array[right_idx]
                    ])

                    left_idx += 1
                    right_idx -= 1
                elif current_sum < targetSum:
                    left_idx += 1
                elif current_sum > targetSum:
                    right_idx -= 1

    return results
