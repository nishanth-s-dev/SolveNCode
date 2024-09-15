# Platform          : Leetcode
# Problem Number    : 15
# Problem Name      : 3Sum
# Problem Topics    : Array, Two Pointer, Sorting
# Problem URL       : https://leetcode.com/problems/3sum


# o(n^3) | o(1)
def three_integer_sum_method_one(numbers):
    res = []
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            for k in range(len(numbers)):
                if i != j and i != k and j != k:
                    current_sum = numbers[i] + numbers[j] + numbers[k]
                    if current_sum == 0:
                        current_vals = [numbers[i], numbers[j], numbers[k]]
                        current_vals.sort()
                        if current_vals not in res:
                            res.append(current_vals)
    return res

# o(n^2) | o(1)
def three_integer_sum_method_two(numbers):
    res = []
    numbers.sort()
    for i in range(len(numbers) - 2):
        if i > 0 and nums[i - 1] == nums[i]:
            continue
        l, r = i + 1, len(numbers) - 1
        while l < r:
            current_sum = numbers[i] + numbers[l] + numbers[r]
            if current_sum < 0:
                l += 1
            elif current_sum > 0:
                r -= 1
            else:
                res.append([numbers[i], numbers[l], numbers[r]])
                while l < r and nums[l + 1] == numbers[l]:
                    l += 1
                while l < r and nums[r - 1] == numbers[r]:
                    r -= 1

                l += 1
                r -= 1
    return res

if __name__ == '__main__':
    # nums = [-15, 13, 6, -11, -4, 5, -13, 5, 3, 2, 6, -1, 4, 12, -10, -13, -7, -4, -5, 6, 9, -14, 1, -6, 13, 7, -8, 10,
    #         -4, 11, -8, -3, 1, 5, -7, 4, -13, -13, -5, -3, 4, -14, 11, -14, 5, -13, -12, 13, -10, -10, -4, -15, 13, 13,
    #         -14, 11, -3, -15, 6, 1, 3, 5, 13, -11, -5, -9, 1, -2, -14, 11, 10, 5, 4, -1, 6, -6, -7, 9, -15, -2, 7, -12,
    #         -10, 5, -14, 13, -6, -9, 6, 7, 7, -6, -2, -3, -9, 0, -5, 7, 5, -4, -5, -7, -13, 14, 7, 8, -15, 7, -5, -15,
    #         -10, 9]
    # nums = [-1, 0, 1, 2, -1, -4]
    nums = [-2,0,0,2,2]
    print(three_integer_sum_method_two(nums))
