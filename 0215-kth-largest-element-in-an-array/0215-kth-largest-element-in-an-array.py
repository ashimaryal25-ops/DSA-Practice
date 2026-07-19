import heapq

class Solution(object):
    def findKthLargest(self, nums, k):
        min_heap = [] 
        
        for num in nums:

            heapq.heappush(min_heap, num)
            
            #check capacity
            if len(min_heap) > k:
                # Kick out the smallest number
                heapq.heappop(min_heap)
                
        return min_heap[0]