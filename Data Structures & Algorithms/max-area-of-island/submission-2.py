class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS,COLS=len(grid), len(grid[0])

        def dfs(r,c):
            if r not in range(0,ROWS) or c not in range(0,COLS) or grid[r][c]==0:
                return 0
            grid[r][c]=0
            area = 1
            for i, j in [[0,1],[1,0],[0,-1],[-1,0]]:
                area += dfs(r+i, c+j)
            return area

        maxArea=0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]==1:
                    maxArea=max(maxArea,dfs(r,c))
                    
        return maxArea