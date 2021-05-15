# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

#  Example 1:
# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
# Example 2:
# Input: intervals = [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.
 
# Constraints:

# 1 <= intervals.length <= 104
# intervals[i].length == 2
# 0 <= starti <= endi <= 104

-----------------------------------SOLUTION-----------------------------------------------------------------

def answer(l):
    if len(l)==0 or len(l)==1:
        return l
    smalloutput=answer(l[1:])
    if l[0][1]>=smalloutput[0][0]:
        return [[l[0][0],smalloutput[0][1]]]+smalloutput[1:]
    else:
        return [l[0]]+smalloutput

l=[[1,3],[2,6],[8,10],[9,12],[14,16],[15,18]]
ans=answer(l)
print(ans)
