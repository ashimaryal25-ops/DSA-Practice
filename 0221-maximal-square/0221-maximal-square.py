class Solution:
    def maximalSquare(self, matrix):
        if not matrix: return 0
        
        rows, cols = len(matrix), len(matrix[0])
        max_side = 0
        
        dp = [[0] * (cols + 1) for _ in range(rows + 1)]
        
        for r in range(rows - 1, -1, -1):
            for c in range(cols - 1, -1, -1):
                
                if matrix[r][c] == '1':
                    
                    dp[r][c] = min(
                        dp[r + 1][c],      # Down
                        dp[r][c + 1],      # Right
                        dp[r + 1][c + 1]   # Bottom-Right
                    ) + 1
                    
                    max_side = max(max_side, dp[r][c])
                    
        return max_side * max_side
        