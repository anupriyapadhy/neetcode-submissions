class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m,n=len(grid),len(grid[0])
        directions=[[0,1],[1,0],[0,-1],[-1,0]]
        islands=0
        def dfs(row,col):
           
            if row<0 or row>=m or col<0 or col>=n or  grid[row][col]=='0':
               
                return
            grid[row][col] = "0"
            for i_off,j_off in directions:
                
                p,k=row+i_off,col+j_off                
                dfs(p,k)

        for i in range(m):
            for j in range(n):
                if grid[i][j]=='1':
                    dfs(i,j)
                    islands+=1
        return islands

        