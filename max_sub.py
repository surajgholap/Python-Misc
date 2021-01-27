def max_grid(grid, max_sum):
    n = len(grid)
    su = [[0]*(n) for _ in range(n)]
    count = 0
    final = 0
    for i in range(n):
        for j in range(n):
            if i == 0 and j == 0:
                su[0][0] = grid[0][0]
            elif j == 0:
                su[i][0] == su[i-1][0]+grid[i][0]
            elif i == 0:
                su[0][j] == su[0][j-1]+grid[0][j]
            else:
                su[i][j] = su[i-1][j]+su[i][j-1]+grid[i][j]-su[i-1][j-1]
            count = max(count, grid[i][j])
    print(su)
    left, right = 0, n
    while left < right:
        mid = left+(right-left+1)//2
        res = 0
        for i in range(mid-1, n):
            for j in range(mid-1, n):
                ans = su[i][j]
                if mid <= i:
                    ans -= su[i-mid][j]
                if mid <= j:
                    ans -= su[i][j-mid]
                if mid <= i and mid <= j:
                    ans += su[i-mid][j-mid]
                res = max(res, ans)
        if res <= max_sum:
            left = mid
        else:
            right = mid - 1

    if max_sum < su[0][0]:
        return 0
    return right - 1


print(max_grid([[1, 1, 1], [1, 1, 1], [1, 1, 1]], 4))
print(max_grid([[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4]], 39))
print(max_grid([[4, 5], [6, 7]], 2))
