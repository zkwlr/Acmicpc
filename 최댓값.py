# B3

import sys

input = sys.stdin.readline

ls = [[int(x) for x in input().split()] for _ in range(9)]

ans = -1
ansx, ansy = 0, 0
for i in range(9):
    for j in range(9):
        if ls[i][j] > ans:
            ans = ls[i][j]
            ansx, ansy = i + 1, j + 1

print(ans)
print(ansx, ansy)
