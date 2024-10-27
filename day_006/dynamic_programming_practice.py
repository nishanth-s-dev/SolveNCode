def fib(n, memo = dict()):
    if n <= 2:
        return n
    if n not in memo:
        memo[n] = fib(n - 1, memo) + fib(n - 2, memo)
    return memo[n]


def main():
    number = int(input("Enter number to find fib: "))
    print(fib(number))

if __name__ == '__main__':
    main()