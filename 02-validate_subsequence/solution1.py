def isValidSubsequence(array, sequence):  # O(n)
    j = 0
    sequence_size = len(sequence)
    for n in array:
        if n == sequence[j]:
            j += 1
            if j == sequence_size:
                return True
    return False


print(isValidSubsequence([5, 1, 22, 25, 6, -1, 8, 10], [1, 6, -1, 10]))
print(isValidSubsequence([5, 1, 22, 25, 6, -1, 8, 10], [5, 1, 22, 6, -1, 8, 10]))
print(isValidSubsequence([5, 1, 22, 25, 6, -1, 8, 10], [1, 6, -1, -1]))
