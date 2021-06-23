import heapq
a=[10,7,2,5,3,4,1,6,9,8]
k=7
heap=a[:k]
heapq._heapify_max(heap)
for i in range(k,len(a)):
    if a[i]<heap[0]:
        heap[0],a[i]=a[i],heap[0]
    heapq._heapify_max(heap)
print(heap)