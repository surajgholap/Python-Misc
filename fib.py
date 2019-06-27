def fib_iter(n):
    a = 1
    b = 1
    if n == 1 or n == 2:
        return a
    for i in range(2, n):
        c = a + b
        # res = c
        a = b
        b = c
    return c


def fib_memo(n, memo):
    if memo[n]:
        return memo[n]
    if n == 1 or n == 2:
        res = 1
    else:
        return fib_memo(n-1, memo) + fib_memo(n-2, memo)
    memo[n] = res
    return res


def rec_fib(n):
    # print("*")
    if n == 1 or n == 2:
        res = 1
    else:
        return rec_fib(n-1) + rec_fib(n-2)
    return res


def fib_driver(num):
    m = [0]*(num+1)
    return fib_memo(num, m)


print(rec_fib(6))
# print(rec_fib(10))

print(fib_driver(10))
print()
print(fib_iter(1))
print(fib_iter(2))
print(fib_iter(3))
print(fib_iter(4))
print(fib_iter(5))
print(fib_iter(6))
print(fib_iter(7))
