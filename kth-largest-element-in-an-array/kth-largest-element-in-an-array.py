from heapq import heapify, heappush, heappop

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Creating empty heap
        heap = []
        heapify(heap)   # transforms list into a heap, in-place, in linear time
        
        for num in nums:
            heappush(heap, num)  # O(Logk)
            if len(heap) > k:
                heappop(heap)  #  remove and return the smallest element O(Logk)
        
        return heappop(heap)
