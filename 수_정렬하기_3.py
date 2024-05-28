# B1

import sys

input = sys.stdin.readline
n = int(input())
ls = [0] * 10001

for _ in range(n):
    ls[int(input())] += 1

for i in range(10001):
    if ls[i] != 0:
        for j in range(ls[i]):
            print(i)
