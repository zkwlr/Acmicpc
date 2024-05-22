# S4

import sys

input = sys.stdin.readline


class Queue:
    ls = []

    def __init__(self):
        self.ls = []

    def push(self, x):
        self.ls.append(x)

    def pop(self):
        if not self.ls:
            return -1
        else:
            tmp = self.ls[0]
            del self.ls[0]
            return tmp

    def size(self):
        return len(self.ls)

    def empty(self):
        return 1 if len(self.ls) == 0 else 0

    def front(self):
        print("-1" if len(self.ls) == 0 else self.ls[0])

    def back(self):
        print("-1" if len(self.ls) == 0 else self.ls[-1])


queue = Queue()

n = int(input())
for _ in range(n):
    ls = [x for x in input().split()]
    a = ls[0]
    if len(ls) > 1:
        b = int(ls[1])
    if a == "push":
        queue.push(b)
    if a == "pop":
        print(queue.pop())
    if a == "front":
        queue.front()
    if a == "back":
        queue.back()
    if a == "size":
        print(queue.size())
    if a == "empty":
        print(queue.empty())
