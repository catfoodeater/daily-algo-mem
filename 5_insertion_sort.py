def swap(array, a, b):
	c = array[a]
	array[a] = array[b]
	array[b] = c

	return array

def sort(array: list):
	i = 0

	while i < len(array):
		t = i

		while t > 0 and array[t] < array[t-1]:
			array = swap(array, t, t-1)

			t = t - 1

		i = i + 1

	return array

arr = [63, 18, 6, 98, 67, 53, 12]

print(f"Array: {arr}, Sorted: {sort(arr)}")
