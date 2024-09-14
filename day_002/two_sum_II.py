# Platform          : Leetcode
# Problem Number    : 167
# Problem Name      : Two Sum II - Input Array Is Sorted
# Problem Topics    : Two Pointer, Array, Binary Search
# Problem URL       : https://leetcode.com/problems/two-sum-ii-input-array-is-sorted


def two_sum(numbers, target):
    l = 0
    r = len(numbers) - 1

    while l < r:
        current_sum = numbers[l] + numbers[r]
        if current_sum < target:
            l += 1
        elif current_sum > target:
            r -= 1
        else:
            return [l + 1, r + 1]

    return [-1]

if __name__ == '__main__':
    print(two_sum([2, 7, 11, 15], 9))