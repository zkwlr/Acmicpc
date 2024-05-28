# S3
import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
box = deque([int(x) for x in range(1, n + 1)])
stack, ans, isans = [], [], True

ls = [int(input()) for _ in range(n)]

for i in range(n):
    while len(stack) == 0 or ls[i] != stack[-1]:
        try:
            stack.append(box.popleft())
            ans.append("+")
        except:  # 빈 box에서 pop하려 하면 불가능한 경우
            isans = False
            break
    stack.pop()  # 예외처리 할필요 X
    ans.append("-")


if isans:
    for i in ans:
        print(i)
else:
    print("NO")
