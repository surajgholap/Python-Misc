
def segment(x, space):
    n = len(space)
    cont = []
    if x == 1:
        return max(space)

    if x > (n/2):
        return min(space)

    for i in range(n-x+1):
        cont.append(min(space[i:i+x]))
    return max(cont)


def segment2(x, space):
    n = len(space)
    if x == 1:
        return max(space)
    if x > (n/2):
        return min(space)
    for i in range(n-x+1):
        if i == 0:
            a = min(space[:x])
        elif a < min(space[i:i+x]):
            a = min(space[i:i+x])
    return a


def counPairs(k, arr):
    ans = []
    for i, n in enumerate(arr):
        if i+k in arr and n != arr.index(i+k):
            a = sorted([i, i+k])
            if a not in ans:
                ans.append(sorted([i, i+k]))
    return len(ans)


print(counPairs(1, [1, 1, 2, 2, 3, 3]))

print(segment(2, [8, 2, 4, 6, 3, 7, 2, 3]))
print(segment(4, [2, 3, 7, 1, 8, 9]))
print(segment(3, [5, 2, 5, 4, 6, 8]))

print(segment2(2, [8, 2, 4, 6, 3, 7, 2, 3]))
print(segment2(4, [2, 3, 7, 1, 8, 9]))
print(segment2(3, [5, 2, 5, 4, 6, 8]))
