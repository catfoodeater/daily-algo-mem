# Forgot to time implementation,
# I would guess no longer than 5 minutes

def sort(array):
	isSorted = False

	while not isSorted:
		isSorted = True

		for index in range(len(array) - 1):
			if array[index] > array[index + 1]:
				oldValue = array[index + 1]
				array[index + 1] = array[index]
				array[index] = oldValue

				isSorted = False

			
	return array

arr = [92, 53, 69, 38, 54, 81, 92, 57]

print(f"Array: {arr}\nSorted: {sort(arr)}")
