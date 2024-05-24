# S5

import sys

input = sys.stdin.readline

ls = [[int(x) for x in input().split()] for _ in range(int(input()))]

# x,y 에서 y(2번째 인자) 오름차순, 그 다음 그 안에서 x(1번째 인자) 오름차순
ls.sort(key=lambda x: (x[1], x[0]))

for i in ls:
    print(i[0], i[1])
