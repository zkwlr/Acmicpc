# B3

import sys

input = sys.stdin.readline

while 1:
    a,b = map(int, input().split())
    if a+b == 0: sys.exit()
    elif a%b == 0: print("multiple")
    elif b%a == 0: print("factor")
    else: print("neither")