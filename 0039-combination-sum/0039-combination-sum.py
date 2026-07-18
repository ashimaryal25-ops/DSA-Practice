class Solution(object):
    def combinationSum(self, candidates, target):
        res = []
        
        def dfs(start_index, current_combo, current_sum):
            if current_sum == target:
                res.append(list(current_combo))
                return
            
            if current_sum > target:
                return
            
            for i in range(start_index, len(candidates)):
                current_combo.append(candidates[i])
                dfs(i, current_combo, current_sum + candidates[i])
                current_combo.pop()

        dfs(0, [], 0)
        return res
        