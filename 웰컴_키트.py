# B3

import sys
from math import ceil

input = sys.stdin.readline

n = int(input())
ls = [int(x) for x in input().split()]
t, p = map(int, input().split())

t_ans, p_ans = 0, 0
for i in ls:
    t_ans += ceil(i / t)

print(t_ans)
print(n // p, n % p)
