s = input()
test = []
c = 0
isredundant = False
for i in s:
    if i in "]})":
        if len(test)==0:
            print("unbalanced parenthesis")
            exit()
        if i == ')':
            while test[-1] != '(':
                test.pop()
                c += 1
            if c == 0:
                isredundant = True
                break
            else:
                test.pop()
                c = 0
        elif i == ']':
            while test[-1] != '[':
                test.pop()
                c += 1
            if c == 0:
                isredundant = True
                break
            else:
                test.pop()
                c = 0
        elif i == '}':
            while test[-1] != '{':
                test.pop()
                c += 1
            if c == 0:
                isredundant = True
                break
            else:
                test.pop()
                c = 0
    else:
        test.append(i)
print(isredundant)