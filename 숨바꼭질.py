# S1

import sys
from collections import deque

input = sys.stdin.readline

dist = [-1] * 100001

q = deque()


def bfs(n, k):

    # 시작 지점 방문 기록
    dist[n] = 0
    # 큐에 n 넣기
    q.append(n)

    dx = [1, -1, 2]
    while q:
        cur_x = q.popleft()
        for nx in cur_x + 1, cur_x - 1, cur_x * 2:

            if nx < 0 or nx > 100000:
                continue
            if dist[nx] >= 0:
                continue

            dist[nx] = dist[cur_x] + 1
            q.append(nx)

    return dist[k]


n, k = map(int, input().split())
print(bfs(n, k))
