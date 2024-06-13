# S2

import sys
import heapq

input = sys.stdin.readline

ls = []

for _ in range(int(input())):
    x = int(input())
    try:
        if x == 0:
            print(heapq.heappop(ls))
        else:
            heapq.heappush(ls, x)
    except IndexError:
        print(0)
