# S4

import sys

input = sys.stdin.readline

n = int(input())

ls = [int(x) for x in input().split()]
ls.sort()

dp = [0] * n
dp[0] = ls[0]
for i in range(1, n):
    dp[i] = dp[i - 1] + ls[i]

print(sum(dp))
