import heapq
class KthLargest:
    #the size of the heap is = k
    #the smallest element in that k size will be the
    #Kth largest element in the whole nums array
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.minHeap = nums
        heapq.heapify(self.minHeap)

        #running a loop here because we do not need our heap size to be more than k
        #nums may have more than k elements so we are decreasing the size of our heap to exactly k
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap,val)

        #if after insertion the size of the heap becomes > k
        #we will pop the element to keep the size = k
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]


        
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)