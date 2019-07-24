def is_anagram(s):
    """
    Returns True if string s is an anagram.

    Arguments:
        s {string} -- String containing chars and numbers.
    """
    stack = []
    for i in s.lower().strip():
        if i.isalnum():
            stack.append(i)
    return stack == stack[::-1]


print(is_anagram("ana"))
print(is_anagram("ana ana"))
print(is_anagram("ana 4ana"))
print(is_anagram("ana454ana"))
print(is_anagram("ana sna"))
print(is_anagram("ana 3wana"))
print(is_anagram("ana 23d4ana"))
print(is_anagram("ana45ana"))
