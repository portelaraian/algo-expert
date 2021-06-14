# O(N) Time Complexity | O(1) Space Complexity
def isValidSubsequence(array, sequence):

    j = 0  # Sequence index
    for i in range(len(array)):
        # Ensuring that will not have an IndexError
        if j <= (len(sequence) - 1):
            if array[i] == sequence[j]:
                j += 1

    return j == len(sequence)
