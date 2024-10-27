def fib(n, memo = dict()):
    if n <= 2:
        return n
    if n not in memo:
        memo[n] = fib(n - 1, memo) + fib(n - 2, memo)
    return memo[n]


def gridTraveler(row, col, memo = dict()):
    if row == 1 and col == 1:
        return 1
    if row < 1 or col < 1:
        return 0

    if (row, col) not in memo:
        memo[(row, col)] = gridTraveler(row - 1, col, memo) + gridTraveler(row, col - 1, memo)

    return memo[(row, col)]


def main():
    print(gridTraveler(22, 33))


if __name__ == '__main__':
    main()