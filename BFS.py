import sys
from collections import deque

input = sys.stdin.readline

board = [
    [1, 1, 1, 0, 1, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [1, 1, 1, 0, 1, 0, 0, 0, 0, 0],
    [1, 1, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]

n = 7  # 행의 수
m = 10  # 열의 수

vis = [[False] * m for _ in range(n)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


q = deque()
vis[0][0] = True
q.append((0, 0))

while q:
    cur_x, cur_y = q.popleft()
    print(f"({cur_x}, {cur_y}) -> ", end=" ")

    for dir in range(4):
        nx = cur_x + dx[dir]
        ny = cur_y + dy[dir]

        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue

        if vis[nx][ny] or board[nx][ny] != 1:
            continue

        vis[nx][ny] = True
        q.append((nx, ny))
