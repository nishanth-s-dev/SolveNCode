def fib(n, memo = dict()):
    if n <= 2: return n

    if n not in memo:
        memo[n] = fib(n - 1, memo) + fib(n - 2, memo)
    return memo[n]


def gridTraveler(row, col, memo = None):
    if memo is None: memo = dict()
    if row == 1 and col == 1: return 1
    if row < 1 or col < 1: return 0

    key = (min(row, col), max(row, col))

    if key not in memo:
        memo[key] = gridTraveler(row - 1, col, memo) + gridTraveler(row, col - 1, memo)

    return memo[key]


def main():
    print(gridTraveler(18, 18))


if __name__ == '__main__':
    main()