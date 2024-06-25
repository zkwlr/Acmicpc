# B3

import sys

input = sys.stdin.readline

while 1:
    ls = list(map(int, input().split()))
    if not ls:
        sys.exit()
    if sum(ls) == 0:
        print("D")
    if sum(ls) == 3:
        print("A")
    if sum(ls) == 2:
        print("B")
    if sum(ls) == 1:
        print("C")
    if sum(ls) == 4:
        print("E")
