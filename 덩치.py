# S5

import sys

input = sys.stdin.readline
n = int(input())
ls = [[int(x) for x in input().split()] for _ in range(n)]

rank = [1] * n

for i in range(n):
    for j in range(n):
        if ls[j][0] > ls[i][0] and ls[j][1] > ls[i][1]:
            rank[i] += 1

for i in rank:
    print(i, end=" ")
