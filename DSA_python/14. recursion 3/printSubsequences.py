def printSubsequences(s,string):
    if s=="":
        print(string)
        return
    printSubsequences(s[1:], string + "")
    printSubsequences(s[1:],string+s[0])

printSubsequences("abc","")