import heapq
from typing import List

class KthLargest:

    def __init__ (self, k: int, nums: List[int]):
        self.k, self.minHeap = k, nums
        heapq.heapify(self.minHeap)
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)
    
    def add (self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        while len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]

kthLargest = KthLargest(3, [100, 89, 70, 23])
kthLargest.add(0)
print(kthLargest.minHeap)