class Solution(object):
    def subsets(self, nums):
        res = []
        
        def dfs(start_index, current_combo):
            res.append(list(current_combo))
            
            for i in range(start_index, len(nums)):
                current_combo.append(nums[i])
                dfs(i + 1, current_combo)
                current_combo.pop()

        dfs(0, [])
        return res