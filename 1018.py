# S4
import sys

input = sys.stdin.readline
n, m = map(int, input().split())
ls = []
ans = 32
for i in range(n):
    row = input().rstrip()
    rowl = []
    for j in row:
        rowl.append(j)
    ls.append(rowl)

for i in range(n - 7):
    for j in range(m - 7):
        cntb, cntw = 0, 0
        for k in range(i, i + 8):
            for l in range(j, j + 8):
                if (k + l) % 2 == 0:  # 0,0이 B거나 W인 경우
                    if ls[k][l] != "B":  # 0,0이 B여야 하는 경우
                        cntb += 1  # 그 경우에서의 색칠 횟수 추가
                    if ls[k][l] != "W":  # 0,0이 W여야 하는 경우
                        cntw += 1
                else:  # 0,1이 B거나 W인 경우
                    if ls[k][l] != "W":
                        cntb += 1
                    if ls[k][l] != "B":
                        cntw += 1
        if ans > min(cntb, cntw):
            ans = min(cntb, cntw)
print(ans)
