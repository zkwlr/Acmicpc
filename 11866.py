# S5
import sys

n, k = map(int, sys.stdin.readline().split())
ls = []
for i in range(n):
    ls.append(i + 1)
for i in range(n):
    print(ls[k * (i + 1) - 1])
    del ls[k * (i + 1) - 1]
