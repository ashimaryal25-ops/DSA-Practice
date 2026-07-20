class Solution:
    def exist(self, board, word):
        rows, cols = len(board), len(board[0])
        
        def dfs(r, c, i):
            # All characters matched
            if i == len(word):
                return True
                
            # Out of bounds, visited, or mismatch
            if r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] != word[i]:
                return False
                
            # Mark current cell as visited
            temp = board[r][c]
            board[r][c] = "#"
            
            # Explore all 4 valid directions
            found = (dfs(r + 1, c, i + 1) or 
                     dfs(r - 1, c, i + 1) or 
                     dfs(r, c + 1, i + 1) or 
                     dfs(r, c - 1, i + 1))
                     
            # Restore state for other paths (backtrack)
            board[r][c] = temp  
            
            return found
            
        # Scan grid for starting points
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0] and dfs(r, c, 0): 
                    return True
                    
        return False
        