# Platform          : Leetcode
# Problem Number    : 1
# Problem Name      : Two Sum
# Problem Topics    : Array, Hashtable
# Problem URL       : https://leetcode.com/problems/two-sum/


def two_sum(nums, target):
    prev_map = {}

    for index, num in enumerate(nums):
        diff = target - num
        if diff in prev_map:
            return [prev_map[diff], index]
        prev_map[num] = index

    return []

if __name__ == '__main__':
    numbers_list = [2, 7, 11, 15]
    target_sum = 9
    print(two_sum(numbers_list, target_sum))