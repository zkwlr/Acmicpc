# S1

import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

board = [[int(x) for x in input().split()] for _ in range(n)]

dist = [[-1] * m for _ in range(n)]
q = deque()

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def bfs():
    for i in range(n):
        for j in range(m):
            if board[i][j] == 2:
                q.append((i, j))
                dist[i][j] = 0
            if board[i][j] == 0:
                # 방문을 기록해서 더이상 dist를 기록하지 못하게 함
                dist[i][j] = 0

    while q:
        cur_x, cur_y = q.popleft()
        for dir in range(4):
            nx, ny = cur_x + dx[dir], cur_y + dy[dir]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if dist[nx][ny] >= 0:
                continue

            dist[nx][ny] = dist[cur_x][cur_y] + 1
            q.append((nx, ny))

    for i in dist:
        for j in i:
            print(j, end=" ")
        print()


bfs()
