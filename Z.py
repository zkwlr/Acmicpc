# G5

import sys

input = sys.stdin.readline

n, r, c = map(int, input().split())


# 1. 함수 정의: r, c가 1 2 3 4 분면인지 확인하고 n의 크기와 위치에 맞게 방문 순서를 반환
# 2^n * 2^n 배열에서 (r,c)를 몇번 째로 방문하는지 반환하는 함수
def z(r, c, n):
    # 2. base condition n = 0
    if n == 0:
        return 0

    # 3. recursion
    # 2사분면
    sqrt = (2 ** (n - 1)) ** 2
    if r < 2 ** (n - 1) and c < 2 ** (n - 1):
        return z(r, c, n - 1)
    # 1사분면
    if r < 2 ** (n - 1) and c >= 2 ** (n - 1):
        return z(r, c - 2 ** (n - 1), n - 1) + sqrt
    # 3사분면
    if r >= 2 ** (n - 1) and c < 2 ** (n - 1):
        return z(r - 2 ** (n - 1), c, n - 1) + 2 * sqrt
    # 4사분면
    if r >= 2 ** (n - 1) and c >= 2 ** (n - 1):
        return z(r - 2 ** (n - 1), c - 2 ** (n - 1), n - 1) + 3 * sqrt


print(z(r, c, n))
