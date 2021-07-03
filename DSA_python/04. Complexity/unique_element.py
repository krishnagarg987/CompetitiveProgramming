# 1st approach
# sort array,store sum and loop through all the array
# a=[6,1,3,6,4,3,1]
# l=len(a)
# a.sort()
# if a[0]!=a[1]:
#     print(a[0])
# elif a[l-1]!=a[l-2]:
#     print(a[l-1])
# for i in range(1,l-1):
#     if a[i]!=a[i-1] and a[i]!=a[i+1]:
#         print(a[i])
#         break

#2nd approach
# take XOR of all array ,XOR  of duplicate elements is zero remaining unique element left
a=[6,1,3,6,4,3,1]
x=0
for i in a:
    x^=i
print(x)
