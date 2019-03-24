a = 1
b = 1
# print(a)
# print(b)
# for i in range(2, 10):
#     c = a + b
#     print(c)
#     a = b
#     b = c
# print(c)


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
    print("*")
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
