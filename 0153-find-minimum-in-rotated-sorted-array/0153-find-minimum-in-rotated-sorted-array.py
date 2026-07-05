class Solution(object):
    def findMin(self, nums):
        low = 0
        high = len(nums) - 1

        while low < high:
            mid = (low + high) // 2

            #The minimum is on the Right
            if nums[mid] > nums[high]:
                low = mid + 1
            
            #The minimum is on the Left (or is mid itself)
            else:
                high = mid

        #low and high are pointing at the exact same number.
        return nums[low]