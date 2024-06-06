# S3

import sys

input = sys.stdin.readline

t = int(input())
dp = [[0, 0] for _ in range(41)]

# table setting
# dp[i][0] = fibonacci(i) 에서 0이 출력된 수
# dp[i][1] = fibonacci(i) 1이 출력된 수
dp[0][0], dp[0][1] = 1, 0
dp[1][0], dp[1][1] = 0, 1
dp[2][0], dp[2][1] = 1, 1

for _ in range(t):
    n = int(input())
    for i in range(3, n + 1):
        dp[i][0] = dp[i - 1][0] + dp[i - 2][0]
        dp[i][1] = dp[i - 1][1] + dp[i - 2][1]
    print(dp[n][0], dp[n][1])
