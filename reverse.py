def reverse(s):
    stack = list(s)
    rev = ""
    while stack:
        rev += stack.pop()
    print(rev)


def recur_reverse(s):
    if len(s) == 0:
        return s
    return recur_reverse(s[1:]) + s[0]


def rev_string(s):
    mid = len(s) // 2
    i = 0
    s = list(s)
    while i != mid:
        s[i], s[-(i+1)] = s[-(i+1)], s[i]
        i += 1
    return "".join(s)


reverse("fds")
print(recur_reverse("gh j"))
print(rev_string("sdfj"))
