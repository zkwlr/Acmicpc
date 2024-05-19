# B2
a = int(input())
b = int(input())
c = int(input())

ans = str(a * b * c)
dic = {}
for i in range(10):
    dic[i] = 0
for chr in ans:
    dic[int(chr)] += 1

for chr in dic:
    print(dic[chr])
