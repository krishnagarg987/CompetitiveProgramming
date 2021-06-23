def checkPalindrome(s):
    if len(s)==0 or len(s)==1:
        return True
    smalloutput=checkPalindrome(s[1:-1])
    if smalloutput:
        if s[0]==s[-1]:
            return True
    return False

s="missiissimj"
print(checkPalindrome(s))
