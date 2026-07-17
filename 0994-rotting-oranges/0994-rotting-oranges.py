from collections import deque

class Solution(object):
    def orangesRotting(self, grid):
        rows, cols = len(grid), len(grid[0])
        q = deque()
        fresh_count = 0
        time = 0
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    fresh_count += 1
                    
        if fresh_count == 0:
            return 0
            
        while q and fresh_count > 0:
            layer_size = len(q)
            
            for _ in range(layer_size):
                row, col = q.popleft()
                
                for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                    nr, nc = row + dr, col + dc
                    
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh_count -= 1
                        q.append((nr, nc))
                        
            time += 1
            
        return time if fresh_count == 0 else -1