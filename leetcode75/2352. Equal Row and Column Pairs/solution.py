from collections import defaultdict

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        # Approach 1: Brute-force
        row_map = defaultdict(int)
        for row in grid:
            row_map[str(row)] += 1
        
        # Check col
        count = 0
        for i in range(len(grid[0])):
            col = [r[i] for r in grid]
            count += row_map[str(col)]
        
        return count
