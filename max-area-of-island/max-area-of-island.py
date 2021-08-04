class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # max counter for the largest existing area we have seen so far
        # loop through the whole matrix (2 for loops)
        # dfs function -> instead of just marking the island, we also add it to count
        # if cell == 1, area += 1
        # return area and do max(max_count, area)
        max_area = 0
        
        def dfs( i: int, j:int) -> int:
            if (i < len(grid) and j < len(grid[0]) and i >= 0 and j >= 0 and grid[i][j] == 1):
                grid[i][j] = 0
                return 1 + dfs(i + 1, j) + dfs(i - 1, j) + dfs(i, j + 1) + dfs(i, j - 1)           
            return 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    max_area = max(max_area, dfs(i, j))
        
        return max_area