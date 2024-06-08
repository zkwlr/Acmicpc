# B3

n, m = map(int, input().split())
ls = [0] * (n + 1)
for _ in range(m):
    i, j, k = map(int, input().split())
    for l in range(i, j + 1):
        ls[l] = k

for i in range(1, n + 1):
    print(ls[i], end=" ")
