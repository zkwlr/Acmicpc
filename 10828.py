# S4

import sys


class Stack:
    ls = []

    def __init__(self):
        self.ls = []

    def push(self, x):
        self.ls.append(x)

    def pop(self):
        return -1 if not self.ls else self.ls.pop()

    def size(self):
        return len(self.ls)

    def empty(self):
        return 1 if len(self.ls) == 0 else 0

    def top(self):
        print("-1" if len(self.ls) == 0 else self.ls[-1])


stack = Stack()

n = int(sys.stdin.readline())
for _ in range(n):

    ls = [x for x in sys.stdin.readline().rstrip().split()]
    a = ls[0]
    if len(ls) > 1:
        b = int(ls[1])
    if a == "push":
        stack.push(b)
    if a == "pop":
        print(stack.pop())
    if a == "top":
        stack.top()
    if a == "size":
        print(stack.size())
    if a == "empty":
        print(stack.empty())
