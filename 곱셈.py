# B3

import sys

input = sys.stdin.readline

ls = [input().rstrip() for _ in range(2)]

print(int(ls[0]) * int(ls[1][2]))
print(int(ls[0]) * int(ls[1][1]))
print(int(ls[0]) * int(ls[1][0]))
print(int(ls[0]) * int(ls[1]))
