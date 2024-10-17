def reverse(x):
    is_negative = True if x < 0 else False

    if is_negative:
        x *= -1

    res = 0
    while x > 0:
        res = (res * 10) + (x % 10)
        x //= 10

    if res > 2 ** 31 - 1:
        return 0
    return -1 * res if is_negative else res

print(reverse(123))