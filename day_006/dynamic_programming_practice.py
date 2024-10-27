def fib(n, memo = None):
    if memo is None: memo = {}
    if n <= 2: return n

    if n not in memo:
        memo[n] = fib(n - 1, memo) + fib(n - 2, memo)
    return memo[n]

def gridTraveler(row, col, memo = None):
    if memo is None: memo = {}
    if row == 1 and col == 1: return 1
    if row < 1 or col < 1: return 0

    key = (min(row, col), max(row, col))

    if key not in memo:
        memo[key] = gridTraveler(row - 1, col, memo) + gridTraveler(row, col - 1, memo)

    return memo[key]

def canSum(targetSum, numbers, memo = None):
    if memo is None: memo = {}

    if targetSum in memo: return memo[targetSum]
    if targetSum == 0: return True
    if targetSum < 0: return False

    for num in numbers:
        if canSum(targetSum - num, numbers, memo):
            memo[targetSum] = True
            return True

    memo[targetSum] = False
    return False

def main():
    print(canSum(300, [7, 14]))

if __name__ == '__main__':
    main()