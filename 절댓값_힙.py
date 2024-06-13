# S1

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
            # 먼저 절댓값이 작은 순으로 정렬, 절댓값이 같으면 수가 작은 순으로 정렬
            heapq.heappush(ls, (abs(x), x))
    except IndexError:
        print(0)
