strings={
    2:'abc',
    3:'def',
    4:'ghi',
    5:'jkl',
    6:'mno',
    7:'pqrs',
    8:'tuv',
    9:'wxyz'
}
def keyboard(n,li):
    if n==0:
        print(li)
        return
    current=n%10
    string=strings[current]
    for char in string:
        keyboard(n//10,char+li)


keyboard(237,"")
