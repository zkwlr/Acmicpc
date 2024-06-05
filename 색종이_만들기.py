# S2

import sys

input = sys.stdin.readline

ans = [0, 0]


def find(ls, n, r, c):
    if n == 1:  # 재귀 종료조건: 한칸 짜리 조각이 되었을 때
        ans[ls[r - 1][c - 1]] += 1
        return ans
    temp = 0
    for i in range(r - n, r):
        for j in range(c - n, c):
            temp += ls[i][j]
    if temp == 0:  # n*n 전부 0이면 하얀 종이
        ans[0] += 1
        return ans
    elif temp == n * n:  # 색종이 n*n 크기와 숫자의 합이 같으면 파란 종이
        ans[1] += 1
        return ans

    # 조각이 같지 않으면 devide and conquer 시작
    find(ls, n // 2, r - (n // 2), c - (n // 2))  # 좌상단
    find(ls, n // 2, r - (n // 2), c)  # 우상단
    find(ls, n // 2, r, c - (n // 2))  # 좌하단
    find(ls, n // 2, r, c)  # 우하단
    return ans


n = int(input())

ls = [[int(x) for x in input().split()] for _ in range(n)]

find(ls, n, n, n)
print(ans[0])
print(ans[1])
