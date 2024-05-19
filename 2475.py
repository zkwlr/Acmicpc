# B5
n = map(int, input().split(" "))
n = list(n)
ans = 0
for i in n:
    ans += i**2
ans = ans % 10
print(ans)
