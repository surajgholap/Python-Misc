# L = int(input())
# N = int(input())
# w = []
# b = []
# for i in range(N):
#     w[i], b[i] = raw_input().split(" ")

# print(w)
n, q = map(int, input().split())
index = []
data = []
a = list(map(int, input().split()))
for i in range(q):
    index = list(map(int, input().split()))
    data[0] = a[index[0]]
    data[1] = a[index[1]]
    x = (sum(data)) // 2
    print(x)