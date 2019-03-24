def facto(n):
    if n <= 1:
        return 1
    else:
        return n * facto(n-1)


def facto1(n):
    mul = 1
    for i in range(1, n+1):
        mul *= i
    return mul

print(facto(3))
print(facto1(3))
