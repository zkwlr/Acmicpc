# S5
import sys

n = int(input())

ls = [[int(x) for x in sys.stdin.readline().split()] for i in range(n)]

ls.sort()
for i in ls:
    print(i[0], i[1])
