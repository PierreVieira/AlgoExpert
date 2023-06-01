def can_get_necessary_number(array, n, necessary_number):
    return necessary_number in array and necessary_number != n


def twoNumberSum(array, target_sum):  # O(n^2)
    for n in array:
        necessary_number = target_sum - n
        if can_get_necessary_number(array, n, necessary_number):
            return [necessary_number, n]
    return []


print(twoNumberSum([3, 5, -4, 8, 11, 1, -1, 6], 10))
