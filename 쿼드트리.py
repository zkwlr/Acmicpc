# S1

import sys

input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().rstrip())) for _ in range(n)]


# 좌표 압축 가능한지 체크용
def check(x, y, n):
    for i in range(x, x + n):
        for j in range(y, y + n):
            if arr[x][y] != arr[i][j]:
                return False
    return True


def func(r, c, n):
    if n == 1:
        return print(arr[r][c], end="")

    h = int(n / 2)

    # 모두 같아서 압축 가능할 때
    if check(r, c, n):
        return print(arr[r][c], end="")

    # 압축 불가능 할때는 괄호 안에 4개 영역을 압축한 결과를 나타냄
    print("(", end="")
    # 왼쪽 위
    func(r, c, h)
    # 오른쪽 위
    func(r, c + h, h)
    # 왼쪽 아래
    func(r + h, c, h)
    # 오른쪽 아래
    func(r + h, c + h, h)
    print(")", end="")


func(0, 0, n)
