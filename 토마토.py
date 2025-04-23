# G5

import sys
from collections import deque

input = sys.stdin.readline

m, n = map(int, input().split())

board = [[int(x) for x in input().split()] for _ in range(n)]

dist = [[-1] * m for _ in range(n)]


def bfs():

    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    q = deque()

    # queue에 bfs 시작점을 전부 넣고 돌려도 잘 작동함
    for i in range(n):
        for j in range(m):
            if board[i][j] == 1:
                dist[i][j] = 0
                q.append((i, j))
            # 길이 없는 칸이면 dist를 0으로 설정
            if board[i][j] == -1:
                dist[i][j] = 0

    while q:
        cur_x, cur_y = q.popleft()
        for dir in range(4):
            nx = cur_x + dx[dir]
            ny = cur_y + dy[dir]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            # 길이 없는 board의 -1 도 dist에서 0으로 기록해놨기 때문에, board를 볼 필요 없다.
            if dist[nx][ny] >= 0:
                continue

            # 토마토 익음(1로 안 바꿔도 queue에 알아서 들어가기 때문에 잘 작동함)
            board[nx][ny] = 1
            dist[nx][ny] = dist[cur_x][cur_y] + 1
            q.append((nx, ny))

    # 접근하지 못한 덜익은 토마토가 있으면(dist에 -1이 존재하면) -1 출력, 2차원 배열에서 최솟값을 구하는 식
    if (min(map(min, dist))) == -1:
        return -1

    return max(map(max, dist))


print(bfs())
