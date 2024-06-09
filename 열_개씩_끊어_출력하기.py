# B3

import sys

input = sys.stdin.readline

str = input().rstrip()
a, b = len(str) // 10, len(str) % 10

for i in range(a):
    print(str[i * 10 : i * 10 + 10])
print(str[a * 10 : a * 10 + b])
