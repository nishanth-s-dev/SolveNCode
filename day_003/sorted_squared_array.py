# Platform          : AlgoExpert
# Problem Name      : Sorted Squared Array
# Difficulty        : Easy
# Category          : Arrays
# Problem URL       : https://www.algoexpert.io/questions/sorted-squared-array

# o(n log n)
def sortedSquaredArray(array):
    # Write your code here.
    res = []
    for num in array:
        res.append(num * num)

    res.sort()
    return res

if __name__ == "__main__":
    print(sortedSquaredArray([-5, -2, 1, 2, 4, 6, 8]))