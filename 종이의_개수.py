# S2

import sys

input = sys.stdin.readline

n = int(input())

arr_k = [[int(x) for x in input().split()] for _ in range(n)]
zero, neg, pos = 0, 0, 0


# 자르고, 잘랐을 때 종이의 갯수를 리턴하는 함수
def func(arr, n):
    global zero, neg, pos
    # base condition
    if n == 1:
        if arr[0][0] == -1:
            neg += 1
        if arr[0][0] == 0:
            zero += 1
        if arr[0][0] == 1:
            pos += 1
        return

    # recursion
    d = int(n / 3)
    flag = False
    for i in range(n):
        for j in range(n):
            if arr[0][0] != arr[i][j]:
                flag = True
                break
        if flag:
            break
    if not flag:
        if arr[0][0] == -1:
            neg += 1
        if arr[0][0] == 0:
            zero += 1
        if arr[0][0] == 1:
            pos += 1
        return

    # 9박스 recursion
    for i in range(0, n, d):
        for k in range(0, n, d):
            # 3*3 회 재귀 (n/d = 3)
            arr_1 = []
            for j in range(i, i + d):
                arr_2 = []
                for l in range(k, k + d):
                    arr_2.append(arr[j][l])
                arr_1.append(arr_2)
            func(arr_1, d)


func(arr_k, n)
print(neg, zero, pos, sep="\n")
