# B1

import sys

input = sys.stdin.readline
n = int(input())
ls = [int(input()) for _ in range(n)]
ls.sort()
dic = {}
for i in range(n):
    dic[i] = ls[i]

for i in dic:
    print(dic[i])
