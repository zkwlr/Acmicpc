# B2

import sys

input = sys.stdin.readline

n, k = int(input()), 0
n -= 1  # input: 1일때는 while 없이 1이 답
while n > 0:
    k += 1
    n = n - k * 6
print(k + 1)
