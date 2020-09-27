def sol(mat):
    rows = set()
    cols = set()
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j] == 0:
                rows.add(i)
                cols.add(j)
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if i in rows:
                mat[i][j] = 0
            if j in cols:
                mat[i][j] = 0


mat = [[0, 2], [2, 1]]
sol(mat)
print(mat)
