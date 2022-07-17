# def factorial(n):
#     if n <= 1:
#         return 1
#     else:
#         return n * factorial(n-1)


# factorial alternative without using recursion
def factor(num):
    fact = 1
    while num > 0:
        fact = fact * num
        num = num - 1
    return fact


def factorial(n):
    f = 1
    while(n > 0):
        f = f * n
        n = n - 1
        yield(n)


print('=' * 40)


if __name__ == '__main__':

    print(factor(5))
    for number in factorial(5):
        print(number)


