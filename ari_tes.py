def rec_conversion(n):
    """
    Recursively converts a decimal number to binary.

    Arguments:
        n {int} -- Decimal number
    """
    if n > 1:
        rec_conversion(n//2)
    print(n % 2, end='')


def toBinary(n):
    return "{0:b}".format(n)


# def find_pattern(n):
    s = toBinary(n)
    print(s)
    if len(s) == 0:
        return False
    else:
        a = list(zip(s, s[1:] + s[:1]))
        print(a)
        if len(a) % 2 != 0:
            a = a[:-1]

        for i in a:
            # #       print(s[i] + s[i+1])
            if i == ('1', '0') or i == ('0', '1'):
                continue
            else:
                return False
    return True
    # s = str(n)


def find_pattern(n):
    s = toBinary(n)
    # print(s)
    if len(s) == 0:
        return False
    else:
        for i in range(len(s)-1):
            print(s[i: i+2])
            if s[i: i+2] == '01' or s[i: i+2] == '10':
                continue
            else:
                return False
    return True


def try_num_string(inp):
    for i in str(inp):
        print(int(i))


if __name__ == "__main__":
    # rec_conversion(8)
    print(find_pattern(2))
    print(find_pattern(3))
    print(find_pattern(4))
    print(find_pattern(5))
    # try_num_string(12343)
