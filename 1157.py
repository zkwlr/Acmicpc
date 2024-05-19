# B1
a = input().upper()

dic = {}
ans = ""
temp = ""
avalue = 0

for chr in a:
    if chr in dic:
        dic[chr] += 1
    else:
        dic[chr] = 1

for chr in dic:
    if avalue < dic[chr]:
        ans = chr
        avalue = dic[chr]
    elif avalue == dic[chr]:
        temp = avalue
if temp == avalue:
    print("?")
else:
    print(ans)
