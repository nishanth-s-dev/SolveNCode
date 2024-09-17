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

if __name__ == "__main__":
    print(sorted_squared_array_method_two([-5, -2, 1, 2, 4, 6, 8]))