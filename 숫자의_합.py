n = int(input())
numstring = input()
numlist = list(numstring)
ans = 0
for i in range(n):
    ans += int(numlist[i])
print(ans)
