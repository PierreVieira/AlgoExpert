def sortedSquaredArray(array):
    return list(sorted(map(lambda x: x ** 2, array)))


print(sortedSquaredArray([1, 2, 3, 5, 6, 8, 9]))
print(sortedSquaredArray([-5, -4, -3, -2, -1]))
print(sortedSquaredArray([-7, -3, 1, 9, 22, 30]))
