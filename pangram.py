def is_pangram(s):
    """
    Returns if s is a pangram(contains all the letters in the alphabet)

    Arguments:
        s {string} -- String used to check if it is a pangram.
    """
    list_alph = set()
    for i in s:
        if i.isalpha():
            list_alph.add(i)
    return len(list_alph) == 26


print(is_pangram("Quick ephyrs blow, vexing daft Jim"))
