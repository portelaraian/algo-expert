# O(n) Time | O(1) Space
# where n is the length of the array
def isMonotonic(array):
    if len(array) < 2:
		return True

	i = 0
	while i+1 <= len(array)-1:
		if array[i] < array[i+1]:
			return _increasing(array, i)
		elif array[i] > array[i+1]:
			return _decreasing(array, i)
		
		i += 1
	
	return True

		
def _increasing(array, i):
	while i+1 <= len(array)-1:
		if array[i] > array[i+1]:
			return False
		i += 1
		
	return True

def _decreasing(array, i):
	while i+1 <= len(array)-1:
		if array[i] < array[i+1]:
			return False
		i += 1
		
	return True
