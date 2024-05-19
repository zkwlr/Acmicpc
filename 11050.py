# B1

n, k = map(int, input().split())
ans = 1
if k == 0:
    ans = 1
else:
    for i in range(k):
        ans = ans * (n - i)
    for i in range(k):
        ans = ans // (i + 1)
print(ans)
