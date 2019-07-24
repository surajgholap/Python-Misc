def rec_conversion(n):
    """
    Recursively converts a decimal number to binary.

    Arguments:
        n {int} -- Decimal number
    """
    if n > 1:
        rec_conversion(n//2)
    print(n % 2, end='')


if __name__ == "__main__":
    rec_conversion(8)
