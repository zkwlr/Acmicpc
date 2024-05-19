# S4
import sys
from queue import Queue

n = int(sys.stdin.readline().rstrip())
q = Queue()
for i in range(n):
    q.put(i + 1)
while q.qsize() - 1:
    q.get()
    q.put(q.get())
print(q.get())
