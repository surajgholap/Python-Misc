def next_num(s):
    res = []
    i = 0
    while i < len(s):
        count = 1
        while i + 1 < len(s) and s[i] == s[i+1]:
            count += 1
            i += 1
        res.append(str(count) + s[i])
        i += 1
    return "".join(res)


def count_say(n):
    start = "1"
    if n == 1:
        return start
    for i in range(1, n):
        start = next_num(start)
    return start


if __name__ == "__main__":
    print(count_say(2))
    print(count_say(3))
    print(count_say(4))
    print(count_say(5))
