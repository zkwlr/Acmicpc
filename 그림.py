# S1

import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

# 기록
vis = [[False] * m for _ in range(n)]

# 보드
board = [[int(x) for x in input().split()] for _ in range(n)]

# 큐
q = deque()

# 좌표

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
# print(board)

cnt = 0
area = 0

for i in range(n):
    for j in range(m):
        # 0이거나, 이미 방문한 곳이면 무시
        if board[i][j] == 0 or vis[i][j] == 1:
            continue
        # 1인데 아직 방문하지 않았다면 BFS 돌려야 함
        vis[i][j] = True
        q.append((i, j))
        # 그림 갯수 추가
        cnt += 1
        # 넓이 초기화
        temp = 1

        # 그림 하나의 탐색
        while q:
            cur_x, cur_y = q.popleft()
            for dir in range(4):
                nx = cur_x + dx[dir]
                ny = cur_y + dy[dir]

                if nx < 0 or nx >= n or ny < 0 or ny >= m:
                    continue
                if vis[nx][ny] or board[nx][ny] != 1:
                    continue

                vis[nx][ny] = True
                q.append((nx, ny))
                temp += 1

        if temp > area:
            area = temp

print(cnt, area, sep="\n")
