# S4

import sys

input = sys.stdin.readline

n, m = map(int, input().split())
dic = {}

for _ in range(n):
    url, passwd = map(str, input().rstrip().split())
    dic[url] = passwd

for _ in range(m):
    print(dic[input().rstrip()])
