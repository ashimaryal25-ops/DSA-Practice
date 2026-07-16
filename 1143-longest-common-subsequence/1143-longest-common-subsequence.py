class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        m = len(text1)
        n = len(text2)
        
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # 2. Sweep the grid starting at index 1
        for r in range(1, m + 1):
            for c in range(1, n + 1):
                
                # Check if characters match 
                if text1[r - 1] == text2[c - 1]:
                    # Letters match
                    dp[r][c] = 1 + dp[r - 1][c - 1]
                else:
                    # No match
                    dp[r][c] = max(dp[r - 1][c], dp[r][c - 1])
                    

        return dp[m][n]
        