for i in range(int(input())):
    n, k = map(int, input().split())
    string = input()
    arr = map(int, input().split())
    if n==1:
        for i in range(k):
            print(0)
    elif n==2:
        for i in arr:
            if string[0]==string[1]:
                if string[0]=='0':
                    string='10'
                else:
                    string='01'
                print(1)
            else:
                if string[0]=='0':
                    string='11'
                else:
                    string='00'
                print(2)
    else:
        initial = 0
        for i in range(n - 1):
            if string[i] == string[i + 1]:
                initial += 2
            else:
                initial += 1
        for i in arr:
            if i==1:
                if string[1]==string[0]:
                    initial-=1
                else:
                    initial+=1
                if string[0]=='0':
                    string='1'+string[i:]
                else:
                    string='0'+string[i:]
            elif i==n:
                if string[n-2]==string[n-1]:
                    initial-=1
                else:
                    initial+=1
                if string[n-1]=='0':
                    string=string[:-1]+'1'
                else:
                    string=string[:-1]+'0'
            else:
                mid=string[i-1]
                pre=string[i-2]
                next=string[i]
                if pre!=next:
                    initial+=0
                else:
                    if mid=='1' and pre=='0':
                        initial+=2
                    elif mid=='1' and pre=='1':
                        initial-=2
                    elif mid=='0' and pre=='1':
                        initial+=2
                    else:
                        initial-=2
                if mid=='0':
                    string=string[:(i-1)]+'1'+string[i:]
                else:
                    string=string[:(i-1)]+'0'+string[i:]
            print(initial)
