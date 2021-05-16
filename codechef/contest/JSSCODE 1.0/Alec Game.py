def is_subseq(x, y):
    it = iter(y)
    return all(any(c == ch for c in it) for ch in x)
    
for i in range(int(input())):
    a,b=input().split()
    if is_subseq(b,a):
        print("AlecWon")
    else:
        print("AlecLost")
    
