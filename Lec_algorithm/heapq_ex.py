import heapq

heap = []

heapq.heappush(heap,4)
heapq.heappush(heap,1)
heapq.heappush(heap,7)
print(heap)

print(heapq.heappop(heap))
print(heap[0])


heap = [1,5,2,8,10]
heapq.heapify(heap)
print(heap)