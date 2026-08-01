class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS= len(grid), len(grid[0])
        directions=[[0,1],[1,0],[0,-1],[-1,0]]
        islands=0
        visited=set()
        def dfs(r,c):
            if r not in range(ROWS) or c not in range(COLS) or grid[r][c]=='0' or (r,c) in visited:
                return 
            visited.add((r,c))
            for dr,dc in directions:
                nr, nc=r+dr, c+dc                                    
                dfs(nr,nc)

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]=='1' and (r, c) not in visited:
                    dfs(r,c)
                    islands+=1
        return islands
        