# S4
import sys

input = sys.stdin.readline

dp = [1002] * 5001  # dp table
dp[1], dp[2], dp[4] = -1, -1, -1  # index error 제거 위해 미리 setting
dp[3], dp[5] = 1, 1  # dp setting - 3kg, 5kg


# +3kg 1회와 +5kg 1회 횟수 추가후 두 거리 중 작은것 택함, 없으면 -1 기록
for i in range(6, 5001):
    if dp[i - 3] != -1:
        dp[i] = dp[i - 3] + 1
    if dp[i - 5] != -1:
        dp[i] = min(dp[i], dp[i - 5] + 1)
    if (
        dp[i] == 1002
    ):  # 초기값일때(만들 수 없을 떄), 1001 의 경우도 나올 수 있음(ex.4999)
        dp[i] = -1

print(dp[int(input())])
