# Platform          : AlgoExpert
# Problem Name      : Sorted Squared Array
# Difficulty        : Easy
# Category          : Arrays
# Problem URL       : https://www.algoexpert.io/questions/sorted-squared-array

# o(n log n)
def sorted_squared_array_method_one(array):
    # Write your code here.
    res = []
    for num in array:
        res.append(num * num)

    res.sort()
    return res

# o(n)
def sorted_squared_array_method_two(array):
    res = []
    if array[0] >= 0:
        for num in array:
            res.append(num ** 2)
        return res

    negative_index = -1
    positive_index = len(array)
    for i in range(len(array)):
        if array[i] >= 0:
            negative_index = i - 1
            positive_index = i
            break
    else:
        negative_index = len(array) - 1

    while negative_index >= 0 and positive_index < len(array):
        negative_value = abs(array[negative_index])
        positive_value = abs(array[positive_index])
        if negative_value > positive_value:
            res.append(positive_value ** 2)
            positive_index += 1
        elif positive_value > negative_value:
            res.append(negative_value ** 2)
            negative_index -= 1
        else:
            res.append(negative_value ** 2)
            res.append(positive_value ** 2)
            positive_index += 1
            negative_index -= 1

    for i in range(negative_index, -1, -1):
        res.append(array[i] ** 2)

    for i in range(positive_index, len(array)):
        res.append(array[i] ** 2)

    return res


"""
Steps:
1. Set two pointers `start` and `end` at the beginning (index 0) and end (index n-1) of the array, respectively.
2. Initialize an empty result array `res` to store squared values in the sorted order.
3. Iterate from the end of the result array towards the start (reverse order):
    - Get the absolute values of `array[start]` and `array[end]`.
    - Compare these two absolute values:
        - If the absolute value at the `end` pointer is greater than or equal to the absolute value at the `start` pointer:
            - Place the square of the value at `end` in the current index of the result array.
            - Decrease the `end` pointer by 1.
        - Else, place the square of the value at `start` in the current index of the result array.
            - Increase the `start` pointer by 1.
4. Continue until all indices in the result array are filled.
5. Return the result array `res`, which now contains the sorted squares of the original array.
"""
def sortedSquaredArrayMethodTwoUpdate(array):
    res = [0 for _ in array]
    start, end = 0, len(array) - 1
    for idx in reversed(range(len(array))):
        start_val = abs(array[start])
        end_val = abs(array[end])
        if start_val < end_val:
            res[idx] = end_val ** 2
            end -= 1
        else:
            res[idx] = start_val ** 2
            start += 1
    return res


if __name__ == "__main__":
    print(sortedSquaredArrayMethodTwoUpdate([1, 2, 3, 5, 6, 8, 9]))