# S3
import sys
from math import *

input = sys.stdin.readline

m, n = map(int, input().split())

ls = [int(x) for x in range(0, n + 1)]
ls[0], ls[1] = 0, 0

# 에라토스테네스의 체
for i in range(2, n + 1, 2):
    if i == 2:
        continue
    ls[i] = 0

for i in range(3, n + 1):
    if i >= sqrt(n + 1):
        break
    if ls[i] == i:
        for j in range(i, n + 1, i):
            if j == i:
                continue
            ls[j] = 0
ls = list(set(ls))
ls.sort()

for i in ls:
    if m <= i:
        print(i)
