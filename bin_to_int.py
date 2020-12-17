inp = "01"
su = 0
for i, j in enumerate(inp[::-1]):
    print(i, j)
    su += int(j) * (2**i)
print(su)
