# S4

import sys

input = sys.stdin.readline

while 1:
    stack = []
    istrue = True

    str = input().rstrip()
    # print(str)
    if str == ".":
        break
        # sys.exit()
    for chr in str:
        if chr == "(":
            stack.append(0)
        elif chr == "[":
            stack.append(1)
        elif chr == ")":
            if len(stack) != 0 and stack[-1] == 0:
                stack.pop()
            else:
                istrue = False
                break
        elif chr == "]":
            if len(stack) != 0 and stack[-1] == 1:
                stack.pop()
            else:
                istrue = False
                break
        else:
            continue

    if len(stack) == 0 and istrue:
        print("yes")
    else:
        print("no")
