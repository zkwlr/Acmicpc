# G5

import sys
import copy
from collections import deque

input = sys.stdin.readline

# 적록 색약은 R과 G를 같은 영역으로 탐색

n = int(input())

board = [list(input().rstrip()) for _ in range(n)]
board1 = copy.deepcopy(board)
for i in range(n):
    for j in range(n):
        if board[i][j] == "G":
            board1[i][j] = "R"


dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def bfs():
    dist = [[0] * n for _ in range(n)]
    q = deque()
    cnt = 0

    for i in range(n):
        for j in range(n):
            if dist[i][j] == 1:
                continue

            dist[i][j] = 1
            q.append((i, j))
            cnt += 1

            while q:
                cur_x, cur_y = q.popleft()
                for dir in range(4):
                    nx, ny = cur_x + dx[dir], cur_y + dy[dir]
                    if nx < 0 or nx >= n or ny < 0 or ny >= n:
                        continue
                    if dist[nx][ny] or board[nx][ny] != board[cur_x][cur_y]:
                        continue

                    dist[nx][ny] = 1
                    q.append((nx, ny))

    return cnt


def bfs2():
    dist = [[0] * n for _ in range(n)]
    q = deque()
    cnt = 0

    for i in range(n):
        for j in range(n):
            if dist[i][j] == 1:
                continue

            dist[i][j] = 1
            q.append((i, j))
            cnt += 1

            while q:
                cur_x, cur_y = q.popleft()
                for dir in range(4):
                    nx, ny = cur_x + dx[dir], cur_y + dy[dir]
                    if nx < 0 or nx >= n or ny < 0 or ny >= n:
                        continue
                    if dist[nx][ny] or board1[nx][ny] != board1[cur_x][cur_y]:
                        continue

                    dist[nx][ny] = 1
                    q.append((nx, ny))

    return cnt


print(bfs(), bfs2(), sep=" ")
