def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)


# factorial alternative without using recursive
def factor(num):
    fact = 1
    while num > 0:
        fact = fact * num
        num = num - 1
    return fact


if __name__ == '__main__':
    print(factorial(10))
    print(factor(10))


