# S4

import sys

input = sys.stdin.readline

n, m = map(int, input().split())

dic1 = {}

for i in range(1, n + 1):
    dic1[input().rstrip()] = str(i)

dic2 = {v: k for k, v in dic1.items()}  # key 와 value 변경하여 탐색속도 높임

for _ in range(m):
    a = input().rstrip()
    if a.isdigit():
        print(dic2[a])
    else:
        print(dic1[a])
