import sys

input = sys.stdin.readline

t = int(input())

ls = [[0] * 15 for _ in range(15)]

for i in range(1, 15):
    ls[0][i] = i

for i in range(t):
    k, n = int(input()), int(input())
    for i in range(1, k + 1):
        for j in range(1, n + 1):
            ls[i][j] = ls[i - 1][j] + ls[i][j - 1]
    print(ls[k][n])
