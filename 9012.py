# S4
import sys

input = sys.stdin.readline


t = int(input().rstrip())


for _ in range(t):
    stack = []
    isans = True
    data = input().rstrip()
    for j in data:
        try:
            if j == "(":
                stack.append(1)
            else:
                stack.pop()
        except:
            isans = False
            break
    if len(stack) == 0 and isans:
        print("YES")
    elif not isans:
        print("NO")
    else:
        print("NO")
