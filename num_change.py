# Find number of ways such that sum is equal to n


def helper(n):
    "Function to call num_change and memoize the total array"
    total = [[0]*(n+1) for _ in range(n+1)]
    if total[n][n] != 0:
        return total[n][n]
    return num_change(n, total)


def num_change(n, total):
    for i in range(n):
        for j in range(n):
            if i == j == 0:
                total[i][j] = 1
            elif i == 0 and j != 0:
                total[i][j] = 0
            else:
                if i > j:
                    total[i][j] = total[i-1][j]
                else:
                    total[i][j] = total[i-1][j] + total[i][j-i]
    return total[n][n]
if __name__ == "__main__":
    a = helper(4)
    print(a)
