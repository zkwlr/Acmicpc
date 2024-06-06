# S3

import sys

input = sys.stdin.readline

n = int(input())

dp = [0] * 1001
dp[1], dp[2] = 1, 3

# 2*n = 2*(n-2)*2 (정사각형 채워넣는 경우/가로로 두칸 넣는경우) + 2*(n-1)
for i in range(3, n + 1):
    dp[i] = (2 * dp[i - 2] + dp[i - 1]) % 10007

print(dp[n])
