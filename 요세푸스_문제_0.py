# S5
import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())
ls = []
dic = {}
idx = k
for i in range(n):
    dic[i+1] = 1

for i in range(n):
    if dic[idx * (i + 1) % n] == 1:
        dic[idx*(i+1)%n] = 0
    else:
        
deq = deque(ls)
print(deq)
