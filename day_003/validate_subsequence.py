# O(n) Time | O(1) space
def isValidSubsequence(array, sequence):
    idx = 0
    for num in array:
        if idx == len(sequence):
            return True
        if num == sequence[idx]:
            idx += 1
    return idx == len(sequence)

if __name__ == "__main__":
    print(isValidSubsequence([1, 2, 3, 4, 5], [1, 2, 5,]))