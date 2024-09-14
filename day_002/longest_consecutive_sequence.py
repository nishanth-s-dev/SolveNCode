# Platform          : Leetcode
# Problem Number    : 128
# Problem Name      : Longest Consecutive Sequence
# Problem Topics    : Array, Hash Table, Union Find
# Problem URL       : https://leetcode.com/problems/longest-consecutive-sequence

# o(n * log n) | o(1)
def longest_consecutive_sequence_method_one(nums):
    if not nums:
        return 0

    nums = sorted(list(set(nums)))
    nums.sort()

    result = 1
    current_result = 1
    for i in range(1, len(nums)):
        diff = nums[i] - nums[i-1]
        if diff == 1:
            current_result += 1
        else:
            result = max(result, current_result)
            current_result = 1

    result = max(current_result, result)

    return result

# o(n) | o(1)
def longest_consecutive_sequence_method_two(nums):
    if not nums:
        return 0

    result = 1

    nums = set(nums)

    for num in nums:
        if num - 1 not in nums:
            current = num
            current_result = 1
            while current + 1 in nums:
                current += 1
                current_result += 1
            result = max(result, current_result)

    return result

if __name__ == "__main__":
    # print(longest_consecutive_sequence_method_one([1,2,0,1]))
    print(longest_consecutive_sequence_method_two([9,1,4,7,3,-1,0,5,8,-1,6]))
