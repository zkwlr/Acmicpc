# S3 # DP

import sys

input = sys.stdin.readline


n = int(input())

dist = [0] * (10**6 + 1)  # 초기 테이블 지정
# dist = [0] * (n + 1)

dist[1] = 0  # 1은 아무 연산이 필요 없다. 초기 테이블 지정

for i in range(2, n + 1):
    dist[i] = dist[i - 1] + 1  # 이전 횟수에 +1을 더한 값
    if i % 2 == 0:
        dist[i] = min(
            dist[i], dist[i // 2] + 1
        )  # 2로 나누어 떨어지면 2로 나눈값의 거리 + 1회 vs +1 연산의 횟수를 비교
    if i % 3 == 0:
        dist[i] = min(
            dist[i], dist[i // 3] + 1
        )  # 3으로 나누어 떨어지면 3으로 나눈 값에서 거리 1 추가 vs +1 연산의 횟수 비교
    # 이 3가지 경우 중 가장 작은 distance가 d[i]의 값
print(dist[n])
