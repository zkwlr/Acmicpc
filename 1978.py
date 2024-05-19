# B2
import sys

input = sys.stdin.readline

n = int(input())
ip = [int(x) for x in input().split()]
cnt = 0
ls = [int(x) for x in range(0, 1001)]
ls[0], ls[1] = 0, 0

# 에라토스테네스의 체
for i in range(2, 1001, 2):
    if i == 2:
        continue
    ls[i] = 0

for i in range(3, 1001):
    if i == 32:
        break
    if ls[i] == i:
        for j in range(i, 1001, i):
            if j == i:
                continue
            ls[j] = 0
ls = set(ls)
for i in ip:
    if i == 0:
        continue
    if i in ls:
        cnt += 1

print(cnt)
