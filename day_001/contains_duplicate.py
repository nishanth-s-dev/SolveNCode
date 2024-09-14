# Platform          : Leetcode
# Problem Number    : 217
# Problem Name      : Contains Duplicate
# Problem Topics    : Array, Hashtable, Sorting
# Problem URL       : https://leetcode.com/problems/contains-duplicate/


def contains_duplicate(arr):
    return len(arr) != len(set(arr))

if __name__ == '__main__':
    print(contains_duplicate([1, 2, 3, 4, 5, 5]))