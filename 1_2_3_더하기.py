# S3

import sys

input = sys.stdin.readline

dp = [0] * 11
dp[1] = 1
dp[2] = 2
dp[3] = 4

# (4 방법) = (3방법 +1) + (2 방법 +2)  + (1 방법 + 3)
# dp[4] = dp[3] + dp[2] + dp[1]
# dp[5] = dp[4] +dp[3] + dp[2] = 13
# 			3 1 1, 1 3 1, 2 2 1, 2 1 1 1, 1 2 1 1, 1 1 2 1, 1 1 1 1 1
# 			3 2, 2 1 2, 1 2 2
# 			2 3, 1 1 3

for i in range(4, 11):
    dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

for _ in range(int(input())):
    print(dp[int(input())])
