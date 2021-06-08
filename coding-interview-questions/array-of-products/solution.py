# O(n²) time | O(n) space
# where n is the length of the array
def arrayOfProducts(array):
    arr_result = []

    for i in range(len(array)):
        product = 1

        for j in range(len(array)):
            if i == j:
                continue

            product *= array[j]

        arr_result.append(product)

    return arr_result
