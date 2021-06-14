# O(n) time | O(n) space - where n is the length of the input array
def firstDuplicateValue(array):
    dict_values = {}

    for value in array:
        try:
            dict_values[value] += 1
            return value
        except:
            dict_values[value] = 1

    return -1
