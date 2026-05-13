def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def factorial(a):
    if a == 0 or a == 1:
        return 1
    else:
        result = 1
        for i in range(2, a + 1):
            result *= i
        return result


def division(a, b):
    return a / b


def multiply(a, b):
    return a * b


def squared(a):
    return a * a
