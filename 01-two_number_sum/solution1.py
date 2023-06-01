def twoNumberSum(array, target_sum):  # O(n^2)
    for i in range(len(array) - 1):
        for j in range(i + 1, len(array)):
            (number1, number2) = array[i], array[j]
            current_sum = number1 + number2
            if current_sum == target_sum:
                return [number1, number2]
    return []


print(twoNumberSum([3, 5, -4, 8, 11, 1, -1, 6], 10))
