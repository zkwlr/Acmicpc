# S5

import sys

input = sys.stdin.readline

s = set()
e = set()
all = {x for x in range(1, 21)}

for _ in range(int(input())):
    ls1 = [x for x in input().split()]
    comm = ls1[0]

    if len(ls1) > 1:
        x = int(ls1[1])
        a = {x}
    if comm == "add":
        s.add(x)
    if comm == "remove":
        try:
            s.remove(x)
        except KeyError:
            pass
    if comm == "check":
        print(1) if s & a else print(0)
    if comm == "toggle":
        s.remove(x) if s & a else s.add(x)
    if comm == "all":
        s = s.union(all)
    if comm == "empty":
        s = s.intersection(e)
