# binary search??? i guess???
# i will time how long it takes next time
# errrrrrrrr

import random
import math

def search(array, target):
	index = math.floor((len(array)-1) / 2)
	t = 0

	while array[index] != target:
		if target > array[index]:
			index += 1
		else:
			index -= 1

		index = math.floor(index)

	return index

arr = [74, 12, 25, 98, 11, 14, 23, 54, 68, 18]
arr.sort()

for i in range(5):
	target = random.choice(arr)
	result = search(arr, target)

	print(f"Target: {target} Index: {result}")
