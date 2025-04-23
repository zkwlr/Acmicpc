# S1

import sys
from collections import deque

input = sys.stdin.readline

t = int(input())

dx = [1, 2, 2, 1, -1, -2, -2, -1]
dy = [2, 1, -1, -2, -2, -1, 1, 2]


def bfs():

    b = int(input())

    x, y = map(int, input().split())
    k, l = map(int, input().split())

    dist = [[-1] * b for _ in range(b)]

    q = deque()

    dist[x][y] = 0
    q.append((x, y))

    while q:
        cur_x, cur_y = q.popleft()

        for dir in range(8):
            nx = cur_x + dx[dir]
            ny = cur_y + dy[dir]

            if nx < 0 or nx >= b or ny < 0 or ny >= b:
                continue
            if dist[nx][ny] >= 0:
                continue

            dist[nx][ny] = dist[cur_x][cur_y] + 1
            q.append((nx, ny))

    return dist[k][l]


for _ in range(t):
    print(bfs())
