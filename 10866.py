# S4

import sys

input = sys.stdin.readline


class Deque:
    ls = []

    def __init__(self):
        self.ls = []

    def push_front(self, x):
        self.ls.insert(0, x)

    def push_back(self, x):
        self.ls.append(x)

    def pop_front(self):
        if not self.ls:
            return -1
        else:
            tmp = self.ls[0]
            del self.ls[0]
            return tmp

    def pop_back(self):
        if not self.ls:
            return -1
        else:
            tmp = self.ls[-1]
            del self.ls[-1]
            return tmp

    def size(self):
        return len(self.ls)

    def empty(self):
        return 1 if len(self.ls) == 0 else 0

    def front(self):
        print("-1" if len(self.ls) == 0 else self.ls[0])

    def back(self):
        print("-1" if len(self.ls) == 0 else self.ls[-1])


deque = Deque()

n = int(input())
for _ in range(n):
    ls = [x for x in input().split()]
    a = ls[0]
    if len(ls) > 1:
        b = int(ls[1])
    if a == "push_front":
        deque.push_front(b)
    if a == "push_back":
        deque.push_back(b)
    if a == "pop_front":
        print(deque.pop_front())
    if a == "pop_back":
        print(deque.pop_back())
    if a == "front":
        deque.front()
    if a == "back":
        deque.back()
    if a == "size":
        print(deque.size())
    if a == "empty":
        print(deque.empty())
