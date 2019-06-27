def perm(l, t='', n=[]):
    if len(l) == 0:
        n.append(t)
    else:
        [perm(l[:i] + l[i+1:], t+l[i], n) for i in range(len(l))]
    return n


if __name__ == "__main__":
    s = 'abcd'
    d = perm(s)
    print(d)
