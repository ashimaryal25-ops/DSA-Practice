class Solution(object):
    def topKFrequent(self, nums, k):
        
        frequents = {}

        for n in nums:

            if n in frequents:
                frequents[n] += 1
            else:
                frequents[n] = 1

        bucket = [ [] for i in range(len(nums) + 1 ) ]

        for key, value in frequents.items():

            bucket[value].append(key)

        topK = []
        for i in range( len(bucket) -1, 0, -1):
            
            for num in bucket[i]:
                topK.append(num)

            if len( topK ) == k:
                return topK    



            



        