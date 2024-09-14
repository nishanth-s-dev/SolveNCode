# Platform          : Leetcode
# Problem Number    : 238
# Problem Name      : Product of Array Except Self
# Problem Topics    : Array, Prefix Sum
# Problem URL       : https://leetcode.com/problems/product-of-array-except-self


# o(n^2) | o(1)
def product_except_self_method_one(nums):
    res = []
    for i in range(len(nums)):
        product = 1
        for j in range(len(nums)):
            if i == j:
                continue
            product *= nums[j]
        res.append(product)
    return res

# o(n) | o(1)
def product_except_self_method_two(nums):
    prefix = prefix_product(nums)
    postfix = postfix_product(nums)

    result = []
    for i in range(len(nums)):
        if i == 0:
            result.append(postfix[i + 1])
        elif i == len(nums) - 1:
            result.append(prefix[i - 1])
        else:
            result.append(prefix[i - 1] * postfix[i + 1])

    return result

# Helper method
def prefix_product(nums):
    current_product = 1
    prefix = [0] * len(nums)
    for i in range(len(nums)):
        current_product *= nums[i]
        prefix[i] = current_product
    return prefix

# Helper method
def postfix_product(nums):
    current_product = 1
    postfix = [0] * len(nums)
    for i in range(len(nums) - 1, -1, -1):
        current_product *= nums[i]
        postfix[i] = current_product
    return postfix

if __name__ == '__main__':
    numbers_list = [1, 2, 3, 4, 5]
    print(product_except_self_method_two(numbers_list))