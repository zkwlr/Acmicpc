import sys

input = sys.stdin.readline
ls = [0] * 5
for i in range(5):
    ls[i] = int(input())

if ls[1] % ls[3] == 0:
    a = ls[1] // ls[3]
else:
    a = ls[1] // ls[3] + 1

if ls[2] % ls[4] == 0:
    b = ls[2] // ls[4]
else:
    b = ls[2] // ls[4] + 1
print(ls[0] - max(a, b))
