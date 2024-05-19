# S5

n = int(input())

ls = [input() for _ in range(n)]
ls = list(set(ls))
ls.sort()
ls.sort(key=lambda x: len(x))

for i in ls:
    print(i)
