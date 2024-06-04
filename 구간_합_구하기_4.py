# S3
# DP, Prefix sum(부분합)
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
ls = list(map(int, input().split()))

dp = [0] * (n + 1)


dp[1] = ls[0]
# O(n)
for i in range(2, n + 1):
    dp[i] = dp[i - 1] + ls[i - 1]

# 탐색당 O(1) -> O(m)
for _ in range(m):
    i, j = map(int, input().split())
    print(dp[j] - dp[i - 1])
