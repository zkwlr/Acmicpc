# B2
list = [int(input()) for _ in range(10)]
dic = {}
for i in list:
    i = i % 42
    if not i in dic:
        dic[i] = 1

print(len(dic))
