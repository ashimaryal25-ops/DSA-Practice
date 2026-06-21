class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        seen = {}

        for i, n in enumerate(nums):

            if n in seen:
                if ( i - seen[n] ) <= k:
                    return True

            seen[n] = i

        return False            

        