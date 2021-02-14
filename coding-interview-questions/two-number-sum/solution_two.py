# O(nlog(n)) time | O(1) Space
def twoNumberSum(array, targetSum):
    # Write your code here.
    array.sort()
    left = 0
    right = len(array) - 1

    while left < right:
        result = array[left] + array[right]
        if result == targetSum:
            return [array[left], array[right]]
        elif result < targetSum:
            left += 1
        else:
            right -= 1

    return []
