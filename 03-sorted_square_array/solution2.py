def sortedSquaredArray(array):  # O(n)
    size = len(array)
    i = 0
    j = size - 1
    copied = [0] * size
    for current_index in reversed(range(size)):
        smaller_value = array[i]
        larger_value = array[j]

        if abs(smaller_value) > abs(larger_value):
            copied[current_index] = smaller_value ** 2
            i += 1
        else:
            copied[current_index] = larger_value ** 2
            j -= 1
    return copied


print(sortedSquaredArray([1, 2, 3, 5, 6, 8, 9]))
print(sortedSquaredArray([-5, -4, -3, -2, -1]))
print(sortedSquaredArray([-7, -3, 1, 9, 22, 30]))
