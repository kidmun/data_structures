def reverse(data):

    start = 0
    end = len(data) - 1
    while start < end:
        data[start], data[end] = data[end], data[start]
        start += 1
        end -= 1

    return ''.join(data)

# O(N) time complexity


def is_palindrome(s):

    data = list(s)
    reversed_string = reverse(data)
    if s == reversed_string:
        return True
    else:
        return False


# def palindrome_python(s):
#
#     if s == s[::-1]:
#         return True
#     else:
#         return False


if __name__ == '__main__':

    print(is_palindrome("madam"))
    # print(palindrome_python("madam"))




