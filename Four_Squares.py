# S3

import sys
import math

input = sys.stdin.readline

n = int(input())

# table setting : n 을 제곱수로 표현하는 제곱수들의 최소 개수
dp = [5] * (n + 4)

tmp = 0
sqrt = []

for i in range(1, n + 1):
    if math.sqrt(i).is_integer():
        dp[i] = 1
        sqrt.append(i)

        dp[i + 1] = min(dp[i + 1], 2 * dp[i])
        dp[i + 2] = min(dp[i + 2], 3 * dp[i])
        dp[i + 3] = min(dp[i + 3], 4 * dp[i])

        if 2 * i <= n:
            dp[2 * i] = min(2, dp[2 * i])
        if 3 * i <= n:
            dp[3 * i] = min(3, dp[3 * i])
        if 4 * i <= n:
            dp[4 * i] = min(4, dp[4 * i])
    else:
        for j in sqrt:
            if dp[i] > dp[j] + dp[i - j]:
                dp[i] = dp[j] + dp[i - j]
                if dp[i] == 2:
                    break


# for i in range(1, 400):
#     print(i, dp[i])
print(dp[n])
