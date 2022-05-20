def reverse(number):
    reversed_integer = 0

    while number > 0:

        remainder = number % 10
        reversed_integer = reversed_integer * 10 + remainder
        number = number // 10

    return reversed_integer


if __name__ == '__main__':
    print(reverse(123))

