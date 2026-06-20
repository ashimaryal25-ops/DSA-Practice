class Solution(object):
    def firstBadVersion(self, n):
        left = 1
        right = n
        
        first_bad = 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if isBadVersion(mid) == True:
                first_bad = mid
                
                right = mid - 1
                
            else:
                left = mid + 1
                
        return first_bad
        