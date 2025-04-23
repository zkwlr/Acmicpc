# S2

import sys
from collections import deque

input = sys.stdin.readline

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

t = int(input())


def bfs():

    cnt = 0
    m, n, k = map(int, input().split())
    board = [[0] * m for _ in range(n)]

    for _ in range(k):
        x, y = map(int, input().split())
        board[y][x] = 1

    dist = [[0] * m for _ in range(n)]
    q = deque()

    for i in range(n):
        for j in range(m):
            if dist[i][j] == 1 or board[i][j] == 0:
                continue
            q.append((i, j))
            cnt += 1
            while q:
                cur_x, cur_y = q.popleft()

                for dir in range(4):
                    nx, ny = cur_x + dx[dir], cur_y + dy[dir]

                    if nx < 0 or nx >= n or ny < 0 or ny >= m:
                        continue
                    if dist[nx][ny] == 1 or board[nx][ny] == 0:
                        continue

                    dist[nx][ny] = 1
                    q.append((nx, ny))

    print(cnt)


for _ in range(t):
    bfs()
