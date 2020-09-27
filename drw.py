def f(v, i, S, F):
    if i >= F:
        if S == 0:
            return 1
        else:
            return 0
    count = f(v, i + 1, S, F)
    count += f(v, i + 1, S - v[i], F)
    return count


"""print(f(v, 0, 12, 2))"""

target = 12
ylist = [1, 2, 3, 4, 5, 6]


def subset_sum(target, F, rolls=[]):
    s = sum(rolls)
    numbers = [1, 2, 3, 4, 5, 6]

    if s == target and len(rolls) == F:
        print(rolls)
    if s >= target:
        return [0]

    for i in range(len(numbers)):
        n = numbers[i]
        subset_sum(target, F, rolls + [n])


print(subset_sum(12, 2))
