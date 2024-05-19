# while 1:
#     try:
#         a, b = map(int, input().split())
#         print(a + b)
#     except:
#         break
# B1
a = input().upper()

dic = {}
ans = 0

for chr in a:
    if chr in dic:
        dic[chr] += 1
    else:
        dic[chr] = 1

for chr in dic:
    if ans < dic[chr]:
        ans = dic[chr]
    elif ans == dic[chr]:
        temp = ans
if temp == ans:
    print("?")
else:
    print(ans)
