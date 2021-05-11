def replace_Pi(s):
    if len(s)==0 or len(s)==1:
        return s
    small_output=replace_Pi(s[1:])
    if s[0:2]=="pi":
        return "3.14"+small_output[1:]
    else:
        return s[0]+small_output

s="ppip"
print(replace_Pi(s))
