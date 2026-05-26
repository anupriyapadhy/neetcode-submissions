class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m,n=len(grid),len(grid[0])
        directions=[[0,1],[1,0],[0,-1],[-1,0]]
        islands=0
        visits=set()
        def dfs(row,col):
           
            if row<0 or row==m or col<0 or col==n or grid[row][col]==0 or (row,col) in visits:               
                return 0
            visits.add((row,col))
            return(1+dfs(row+1,col)+
            dfs(row,col+1)+
            dfs(row-1,col)+
            dfs(row,col-1)
            )
        for i in range(m):
            for j in range(n):
                                           
                islands=max(islands,dfs(i,j))
        return islands
