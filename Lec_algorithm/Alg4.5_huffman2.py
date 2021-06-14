import heapq_ex
from collections import defaultdict

def encode(frequency):
    heap = [[weight, [symbol, '']] for symbol, weight in frequency.items()]
    print(heap)
    heapq_ex.heapify(heap)
    while len(heap) > 1:
        left = heapq_ex.heappop(heap)
        print("LLL",left,left[1:])
        right = heapq_ex.heappop(heap)
        print("HHH",right)
        for pair in left[1:]:
            print("PPP",pair, pair[1])
            pair[1] = '0' + pair[1]
        for pair in right[1:]:
            pair[1] = '1' + pair[1]
        print("OOO",[left[0] + right[0]])
        print("RRR", left[1:] + right[1:])
        print("SSS",[left[0] + right[0]] + left[1:] + right[1:])
        heapq_ex.heappush(heap, [left[0] + right[0]] + left[1:] + right[1:])
#    print("WWW",heapq.heappop(heap)[1][1])
#    print("WWW",heapq.heappop(heap)[1:])
#    print("WWW",heapq.heappop(heap))
    return sorted(heapq_ex.heappop(heap)[1:], key=lambda p: (len(p[1]), p))
data="fuLL"
frequency = defaultdict(int)

for symbol in data:
    frequency[symbol] += 1

huff = encode(frequency)
print ("Symbol".ljust(10) + "Weight".ljust(10) + "Huffman Code")
for p in huff:
    print("AAA",p)
    print("KKK",p[0],frequency[p[0]])
    print (p[0].ljust(10) + str(frequency[p[0]]).ljust(10) + p[1])
