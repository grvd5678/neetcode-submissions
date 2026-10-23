import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.minHeap = nums
        
        # Traditionally transform the list into a min-heap in O(n) time
        heapq.heapify(self.minHeap)
        
        # Pop off the smallest elements until we only have the top k left
        while len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        # Push the new value into our VIP heap
        heapq.heappush(self.minHeap, val)
        
        # If the heap got too big, kick out the smallest one!
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
            
        # The kth largest is always sitting right at the top
        return self.minHeap[0]