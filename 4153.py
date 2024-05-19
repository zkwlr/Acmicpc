# B3
import sys

input = sys.stdin.readline

while 1:
    a, b, c = map(int, input().rstrip().split())
    ls = [a, b, c]
    ls.sort()

    if a == 0 and b == 0 and c == 0:
        break
    else:
        if ls[0] ** 2 + ls[1] ** 2 == ls[2] ** 2:
            print("right")
        else:
            print("wrong")
