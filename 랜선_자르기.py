# S2

import sys

input = sys.stdin.readline

k, n = map(int, input().split())

ls = [int(input()) for _ in range(k)]


start, end = 0, max(ls) + 1


def search(target):
    a = 0
    for k in ls:
        a += k // target
    return a


# n 개 이상이 나오는 길이의 최댓값을 찾는 대신 n개 미만이 나오는 길이의 최솟값을 찾은 후 -1 한다.
# 케이스를 줄일 수 있으므로(>= 를 찾는거보다 < 하나를 찾고 답을 재연산하는게 빠름)
# 즉, 여집합의 답에서 간단하게 원래 연산으로 돌릴 수 있으면 그 방법을 사용하는게 빠르다
# 정석 이분탐색 방법도 찾아보기
while start < end:
    mid = (start + end) // 2
    if search(mid) < n:
        end = mid
    else:
        start = mid + 1

print(start - 1)
