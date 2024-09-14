# Platform          : Leetcode
# Problem Number    : 704
# Problem Name      : Binary Search
# Problem Topics    : Array, Binary Search
# Problem URL       : https://leetcode.com/problems/binary-search

def binary_search(nums, target):
    l, r = 0, len(nums) - 1

    while l <= r:
        mid = (l + r) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    return -1

if __name__ == "__main__":
    print(binary_search([1, 2, 3, 4, 5], 5))