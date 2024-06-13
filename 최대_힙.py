# S2

import sys
import heapq

input = sys.stdin.readline

ls = []

for _ in range(int(input())):
    x = int(input())
    try:
        if x == 0:
            print(heapq.heappop(ls)[1])
        else:
            heapq.heappush(
                ls, (-x, x)
            )  # Max Heap 을 tuple을 통해 구현(앞의 값 기준으로 정렬)
    except IndexError:
        print(0)
