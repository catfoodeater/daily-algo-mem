# I used wikipediap age on merge sort for this
# I found it very difficult but was satisfying when it worked

import math

def sort(array):
	if len(array) < 2:
		return array
	
	left, right = [], []

	for idx in range(len(array)):
		if idx < len(array) / 2:
			left.append(array[idx])
		else:
			right.append(array[idx])

	left = sort(left)
	right = sort(right)

	return merge(left, right)

def merge(left, right):
	while len(left) > 0 and len(right) > 0:
		if left[0] <= right[0]:
			left.append(right[0])
			right.remove(right[0])
		else:
			right.append(left[0])
			left.remove(left[0])

	if len(left) > 0:
		return left
	else:
		return right

arr = [5, 23, 1, 2, 79, 24, 3, 4]

print(f"Array: {arr}, Sorted: {sort(arr)}")
