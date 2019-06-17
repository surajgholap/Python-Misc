def sum_134(n):
    "Return num of ways n can be represented as a sum of 1, 3, 4."
    sum_num = []
    for i in range(3):
        sum_num.append(1)
    sum_num.append(2)
    for i in range(4, n+1):
        sum_num.append(sum_num[i-1] + sum_num[i-3] + sum_num[i-4])
    return sum_num[n]

if __name__ == "__main__":
    print(sum_134(3))
