# S1

import sys

input = sys.stdin.readline

a, b, c = map(int, input().split())


def pow(a, b):
    # base condition (n = 1)
    if b == 1:
        return a % c

    # a^k를 알면 a^2k 나 a^(k+1)도 O(1) 안에 알 수 있다.
    # n = k 일때 n = k + 1이 만족한다.
    if b % 2 == 1:
        return (pow(a, b - 1) * a) % c
    else:
        return (pow(a, b // 2) ** 2) % c


print(pow(a, b))
