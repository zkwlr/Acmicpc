# S5
import sys

input = sys.stdin.readline

n = int(input().strip())

ls = [[x for x in input().split()] for _ in range(n)]

ls.sort(key=lambda x: x[0])

for i in ls:
    print(i[0], i[1])
