# Platform          : Leetcode
# Problem Number    : 347
# Problem Name      : Top K Frequent Element
# Problem Topics    : Array, Hash Table, Divide and Conquer, Sorting, Heap, Bucket Sort, Counting, Quickselect
# Problem URL       : https://leetcode.com/problems/top-k-frequent-elements/


from collections import Counter

def top_k_frequent(nums, k):
    frequency = sorted(Counter(nums).items(), key=lambda field: field[1], reverse=True)

    res = []
    for key, value in frequency:
        if k <= 0:
            break
        res.append(key)
        k -= 1

    return res

if __name__ == '__main__':
    numbers_list = [1, 2, 2, 3, 3, 3]
    print(top_k_frequent(numbers_list, 2))