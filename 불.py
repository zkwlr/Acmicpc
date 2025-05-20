# G4

import sys
from collections import deque

input = sys.stdin.readline

t = int(input())

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def bfs():
    m, n = map(int, input().split())

    board = [list(input().rstrip()) for _ in range(n)]

    fdist = [[-1] * m for _ in range(n)]
    dist = [[-1] * m for _ in range(n)]

    fq, q = deque(), deque()

    for i in range(n):
        for j in range(m):
            if board[i][j] == "#":
                fdist[i][j] = 0
                dist[i][j] = 0
            if board[i][j] == "*":
                fdist[i][j] = 0
                fq.append((i, j))
            if board[i][j] == "@":
                dist[i][j] = 0
                q.append((i, j))

    while fq:
        cur_x, cur_y = fq.popleft()
        for dir in range(4):
            nx, ny = cur_x + dx[dir], cur_y + dy[dir]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if fdist[nx][ny] >= 0:
                continue

            fdist[nx][ny] = fdist[cur_x][cur_y] + 1
            fq.append((nx, ny))

    while q:
        cur_x, cur_y = q.popleft()
        for dir in range(4):
            nx, ny = cur_x + dx[dir], cur_y + dy[dir]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                return dist[cur_x][cur_y] + 1

            # 이미 방문했으면 큐에 넣을 필요 없는데 빼먹음
            if dist[nx][ny] >= 0:
                continue

            if fdist[nx][ny] != -1 and dist[cur_x][cur_y] + 1 >= fdist[nx][ny]:
                # 방문한 것만 기록
                dist[nx][ny] = 0
                continue

            dist[nx][ny] = dist[cur_x][cur_y] + 1
            q.append((nx, ny))

    ans = -1
    for i in range(n):
        if i == 0 or i == n - 1:
            for j in range(m):
                if dist[i][j] <= 0:
                    continue
                else:
                    ans = max(ans, dist[i][j] + 1)
        else:
            if dist[i][0] > 0:
                ans = max(ans, dist[i][0] + 1)
            if dist[i][m - 1] > 0:
                ans = max(ans, dist[i][m - 1] + 1)

    if ans == -1:
        return "IMPOSSIBLE"
    else:
        return ans


for _ in range(t):
    print(bfs())
