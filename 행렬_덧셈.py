# B3

import sys

input = sys.stdin.readline

n, m = map(int, input().split())

ls1 = [[int(x) for x in input().split()] for _ in range(n)]

ls2 = [[int(x) for x in input().split()] for _ in range(n)]

ls3 = [[0 for _ in range(m)] for _ in range(n)]

for i in range(n):
    for j in range(m):
        ls3[i][j] = ls1[i][j] + ls2[i][j]

for i in ls3:
    for j in i:
        print(j, end=" ")
    print()
