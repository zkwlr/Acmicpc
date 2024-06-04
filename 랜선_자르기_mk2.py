# S2

import sys

input = sys.stdin.readline

k, n = map(int, input().split())

ls = [int(input()) for _ in range(k)]

start, end = 1, max(ls)


# 랜선의 길이에 따라 만들 수 있는 랜선의 갯수 계산
def check(target):
    a = 0
    for i in ls:
        a += i // target
    return a


while start <= end:
    mid = (start + end) // 2

    if check(mid) >= n:
        start = mid + 1
    else:
        end = mid - 1

print(end)
