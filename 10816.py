# S4
import sys

input = sys.stdin.readline

n = int(input().rstrip())

ls1 = [int(x) for x in input().rstrip().split()]
m = int(input().rstrip())
ls2 = [int(x) for x in input().rstrip().split()]
dic = {}

result = [0] * m

for num in ls1:
    if num in dic:
        dic[num] += 1
    else:
        dic[num] = 1

for num in ls2:
    if num in dic:
        print(dic[num], end=" ")
    else:
        print(0, end=" ")
