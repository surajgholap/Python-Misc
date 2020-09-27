
def strStr(haystack: str, needle: str):
    if len(needle) == 0:
        return 0
    if needle in haystack:
        return haystack.index(needle)
    else:
        return -1


haystack = "hello"
needle = "ll"
print(strStr(haystack, needle))
