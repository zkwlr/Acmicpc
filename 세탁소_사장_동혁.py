# B3

import sys

input = sys.stdin.readline

t = int(input())
ans = [0] * 4
for _ in range(t):
    c = int(input())
    ans[0] = c // 25
    c %= 25
    ans[1] = c // 10
    c %= 10
    ans[2] = c // 5
    c %= 5
    ans[3] = c
    for i in ans:
        print(i, end=" ")
    print()
