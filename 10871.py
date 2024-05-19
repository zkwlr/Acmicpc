# B5

n, x = map(int, input().split())

list = [int(i) for i in input().split()]
list2 = []
for i in list:
    if i < x:
        list2.append(i)

for i in range(len(list2)):
    print(list2[i], end=" ")
