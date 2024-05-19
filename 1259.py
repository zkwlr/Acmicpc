# B1
while 1:
    stack = []
    a = input()
    if int(a) == 0:
        break
    elif len(a) == 1:
        print("yes")
    else:
        if len(a) % 2 == 0:
            for i in range(len(a) // 2):
                stack.append(a[i])
            for i in range(len(a) // 2, len(a)):
                if stack[-1] == a[i]:
                    stack.pop()
                    if len(stack) == 0:
                        print("yes")
                        break
                else:
                    print("no")
                    break
        else:
            for i in range(len(a) // 2):
                stack.append(a[i])
            for i in range(len(a) // 2 + 1, len(a)):
                if stack[-1] == a[i]:
                    stack.pop()
                    if len(stack) == 0:
                        print("yes")
                        break
                else:
                    print("no")
                    break
