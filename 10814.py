# S5
import sys

input = sys.stdin.readline

n = int(input().strip())

ls = [[x for x in input().split()] for _ in range(n)]

for i in range(n):
    ls[i][0] = int(ls[i][0])
    ls[i].append(i)

ls.sort(key=lambda x: (x[0], x[2]))

for i in ls:
    print(i[0], i[1])
