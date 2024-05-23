# S5

import sys

input = sys.stdin.readline

n = int(input())
ans = []
num = 0

for _ in range(n):
    while 1:
        num += 1
        if "666" in str(num):
            ans.append(num)
            break

print(ans[n - 1])
