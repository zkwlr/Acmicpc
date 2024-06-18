# B1

import sys

input = sys.stdin.readline

n = int(input())
ans, cnt = n, 0

while 1:
    cnt += 1
    n = (n % 10) * 10 + (n // 10 + n % 10) % 10
    if ans == n:
        break

print(cnt)
