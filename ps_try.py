
def sol(arr):
    count = 0
    res = []
    for i in arr:
        if i == 1:
            count += 1
        else:
            if count != 0:
                res.append(count)
                count = 0
                res.append(1)
            else:
                res.append(1)
    if count != 0:
        res.append(count)
    return res


t1 = [2, 3, 0, 1, 1]
t2 = [1, 1, 1, 3, 0, 1]
t3 = [0, 1, 1]
t4 = [0, 3, 4, 1, 1, 1, 5, 3]
t5 = [0, 1, 1, 3, 2, 4, 2, 1, 1, 1]

print(sol(t1))
print(sol(t2))
print(sol(t3))
print(sol(t4))
print(sol(t5))
