def perm(l, t='', n=[]):
    if len(l) == 0:
        n.append(t)
    else:
        for i in range(len(l)):
            perm(l[:i] + l[i+1:], t+l[i], n)
    return n
if __name__ == "__main__":
    s = ['a', 'b', 'c']
    d = perm(s)
    print(set(d))
