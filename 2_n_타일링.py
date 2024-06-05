# S3

import sys

input = sys.stdin.readline

n = int(input())

dp = [0] * 1001
# table setting
dp[1], dp[2] = 1, 2

# 2*n = 2*(n-1)를 채우는 방법 수(세로로 붙이기) + 2*(n-2)을 채우는 방법수 (가로로 2개 쌓기)
for i in range(3, n + 1):
    dp[i] = dp[i - 1] + dp[i - 2]

print(dp[n] % 10007)
