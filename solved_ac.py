# S4

import sys

input = sys.stdin.readline


# 파이썬 round함수의 오류로 인해 삼항 연산자로 직접 반올림 함수 구현
def round2(num):
    return int(num) + (1 if num - int(num) >= 0.5 else 0)


ls = []
n = int(input())
if n == 0:
    print(0)
    sys.exit()

for _ in range(n):
    ls.append(int(input()))

a = round2(n * 15 / 100)

ls.sort()
print(round2(sum(ls[a : n - a]) / (n - 2 * a)))
