# S1

import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

board = [list(map(int, input().rstrip())) for _ in range(n)]

dist = [[-1] * m for _ in range(n)]


def bfs():

    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    q = deque()

    # 초기 거리 설정
    dist[0][0] = 0
    # queue에 시작 지점 삽입
    q.append((0, 0))

    while q:
        cur_x, cur_y = q.popleft()
        for dir in range(4):
            nx = cur_x + dx[dir]
            ny = cur_y + dy[dir]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if dist[nx][ny] >= 0 or board[nx][ny] != 1:
                continue

            dist[nx][ny] = dist[cur_x][cur_y] + 1
            q.append((nx, ny))

    return dist[n - 1][m - 1] + 1


print(bfs())
