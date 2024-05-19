# S4
import sys

input = sys.stdin.readline
n = int(input())
# ls1 = [int(x) for x in input().split()]
ls1 = set(int(x) for x in input().rstrip().split())
m = int(input())
ls2 = [int(x) for x in input().rstrip().split()]

for i in ls2:
    if i in ls1:
        print("1")
    else:
        print("0")
