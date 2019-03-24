
arr = [5, 9, 2, 8, 5, 1]
vis = [0, 0, 0, 0, 0, 0]
lis = []
for i in range(len(arr)):
    if 10-arr[i] in arr and vis[arr.index(10-arr[i])] == 0:
        # if arr[i] + arr[j] == 10:
        lis.append((arr[i], 10 - arr[i]))
        vis[i] = 1
        vis[arr.index(10-arr[i])] = 1
print(lis)
