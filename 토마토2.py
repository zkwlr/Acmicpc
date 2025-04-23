# G5

import sys
from collections import deque

input = sys.stdin.readline

m, n, h = map(int, input().split())

board3d = []
for i in range(h):
    board3d.append([[int(x) for x in input().split()] for _ in range(n)])

dist = []
for i in range(h):
    dist.append([[-1] * m for _ in range(n)])


def bfs():

    dx = [1, 0, -1, 0, 0, 0]
    dy = [0, 1, 0, -1, 0, 0]
    dz = [0, 0, 0, 0, 1, -1]
    q = deque()

    # queue에 bfs 시작점을 전부 넣고 돌려도 잘 작동함
    for i in range(n):
        for j in range(m):
            for k in range(h):
                if board3d[k][i][j] == 1:
                    dist[k][i][j] = 0
                    q.append((i, j, k))
                # 길이 없는 칸이면 dist를 0으로 설정
                if board3d[k][i][j] == -1:
                    dist[k][i][j] = 0

    while q:
        cur_x, cur_y, cur_z = q.popleft()
        for dir in range(6):
            nx = cur_x + dx[dir]
            ny = cur_y + dy[dir]
            nz = cur_z + dz[dir]

            if nx < 0 or nx >= n or ny < 0 or ny >= m or nz < 0 or nz >= h:
                continue
            # 길이 없는 board의 -1 도 dist에서 0으로 기록해놨기 때문에, board를 볼 필요 없다.
            if dist[nz][nx][ny] >= 0:
                continue

            # 토마토 익음(1로 안 바꿔도 queue에 알아서 들어가기 때문에 잘 작동함)
            board3d[nz][nx][ny] = 1
            dist[nz][nx][ny] = dist[cur_z][cur_x][cur_y] + 1
            q.append((nx, ny, nz))

    # 접근하지 못한 덜익은 토마토가 있으면(dist에 -1이 존재하면) -1 출력, 3차원 배열에서 최솟값을 구하는 식
    min_val = min(x for plane in dist for row in plane for x in row)
    if min_val == -1:
        return -1

    max_val = max(x for plane in dist for row in plane for x in row)
    return max_val


print(bfs())
