def twoNumberSum(array, target_sum):  # O(n)
    nums = set()
    for num in array:
        necessary_number = target_sum - num
        if necessary_number in nums:
            return [necessary_number, num]
        else:
            nums.add(num)
    return []


print(twoNumberSum([3, 5, -4, 8, 11, 1, -1, 6], 10))
