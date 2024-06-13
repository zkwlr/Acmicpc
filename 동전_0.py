# S3
# Greedy

import sys

input = sys.stdin.readline

n, k = map(int, input().split())
ls = [int(input()) for _ in range(n)]
ls.sort(reverse=True)

ans, i = 0, 0

while k != 0:
    ans += k // ls[i]
    k %= ls[i]
    i += 1

print(ans)
