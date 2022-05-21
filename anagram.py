def is_anagram(str1, str2):

    if len(str1) != len(str2):
        return False

    str1.sort()
    str2.sort()

    if str1 != str2:
        return False
    else:
        return True


if __name__ == '__main__':
    print(is_anagram(['f', 'l', 'u', 's', 't', 'e', 'r'], ['r', 'e', 's', 't', 'f', 'u', 'l']))
