# S3
import sys

input = sys.stdin.readline

n = int(input())
# 계단 점수 리스트
ls = [0] * 301

# dp[i][j] = 지금까지 j개의 계단을 연속해서 밟고 올라갔을 떄 i번쨰 계단까지의 합의 최대
# table 2개가 필요하다.
dp = [[0 for _ in range(3)] for _ in range(301)]
for i in range(1, n + 1):
    ls[i] = int(input())

# setting
dp[1][1] = ls[1]
dp[2][1] = ls[2]
dp[2][2] = dp[1][1] + ls[2]
dp[3][1] = dp[1][1] + ls[3]
dp[3][2] = dp[2][1] + ls[3]

for i in range(4, n + 1):
    dp[i][1] = max(dp[i - 2][1], dp[i - 2][2]) + ls[i]
    dp[i][2] = dp[i - 1][1] + ls[i]

print(max(dp[n][1], dp[n][2]))
