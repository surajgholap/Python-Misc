
def num_strokes(grid):
    if not grid:
        return 0

    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] != '#':
                color = grid[i][j]
                dfs(grid, i, j, color)
                count += 1
            # print(grid)
        # break
    return count


def dfs(grid, i, j, color):
    if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j]\
            != color:
        return
    grid[i][j] = '#'
    dfs(grid, i+1, j, color)
    dfs(grid, i-1, j, color)
    dfs(grid, i, j+1, color)
    dfs(grid, i, j-1, color)
    # print(grid)
    # count += 1


picture = ["aabba", "aabba", "aaacb"]
# picture = ["aab", "aab"]
rows = len(picture)
cols = len(picture[0])
mat = [[0] * cols for i in range(rows)]

for i in range(rows):
    for j in range(cols):
        mat[i][j] = picture[i][j]
for i in mat:
    print(i)
print(num_strokes(mat))
