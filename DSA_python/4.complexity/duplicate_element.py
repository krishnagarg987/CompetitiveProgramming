# duplicate in array 
# n elemnts given from 0 to n-2 and there is one duplicate ,total elements n-1
# 1st approach
# sort array and go through all elements and look at adjacent elements
# n=7
# a=[5,1,3,0,2,4,1]
# a.sort()
# if a[0]==a[1]:
#     print(a[0])
# elif a[n-1]==a[n-2]:
#     print(a[n-1])
# else:
#     for i in range(1,n-1):
#         if a[i-1]==a[i] or a[i]==a[i+1]:
#             print(a[i])
#             break

# 2nd approach
# sum of all elements and take difference from sum of n elements
n=7
a=[5,1,3,0,2,4,1]
s=sum(a)
actual_sum=((n-2)*(n-1))//2
print(s-actual_sum)
